#!/usr/bin/env bash
# Deploy the cbio-kb chat API to Cloud Run.
#
# Uses Cloud Build to build the image from Dockerfile.chat (so we don't
# need a local Docker build on the caller's machine) and gcloud run deploy
# to push a new revision.
#
# Prereqs (one-time, per-project):
#   - Artifact Registry repo exists:
#       gcloud artifacts repositories create cbio-kb \
#         --location=us-central1 --repository-format=docker
#   - Secret Manager secret exists:
#       echo -n "<sk-ant-...>" | gcloud secrets create anthropic-api-key --data-file=-
#   - Cloud Run runtime service account has:
#       roles/datastore.user          (Firestore)
#       roles/secretmanager.secretAccessor  (to pull the secret at boot)
#   - Firestore Native-mode database exists in the same region.
#
# Usage:
#   scripts/deploy-chat.sh              # deploy to default project/region
#   PROJECT_ID=... REGION=... scripts/deploy-chat.sh

set -euo pipefail

PROJECT_ID="${PROJECT_ID:-cbioportal-python}"
REGION="${REGION:-us-central1}"
SERVICE_NAME="${SERVICE_NAME:-cbio-kb-api}"
REPO_NAME="${REPO_NAME:-cbio-kb}"
IMAGE_TAG="${IMAGE_TAG:-$(git rev-parse --short HEAD 2>/dev/null || date +%s)}"
IMAGE_URI="${REGION}-docker.pkg.dev/${PROJECT_ID}/${REPO_NAME}/${SERVICE_NAME}:${IMAGE_TAG}"

# CORS origins for the chat page — override if your github.io URL differs.
CORS_ORIGINS="${CHAT_CORS_ORIGINS:-https://jim-bo.github.io,http://localhost:8080,http://127.0.0.1:8080}"

echo "=== cbio-kb chat API deploy ==="
echo "Project:  ${PROJECT_ID}"
echo "Region:   ${REGION}"
echo "Service:  ${SERVICE_NAME}"
echo "Image:    ${IMAGE_URI}"
echo "CORS:     ${CORS_ORIGINS}"
echo

# 1. Build & push the image via Cloud Build (remote build, no local Docker).
#    We pass an inline cloudbuild config so we can point at Dockerfile.chat
#    (gcloud builds submit --tag only works with the default ./Dockerfile).
echo ">>> Submitting build to Cloud Build..."
gcloud builds submit \
    --project="${PROJECT_ID}" \
    --config=/dev/stdin <<EOF
steps:
  - name: gcr.io/cloud-builders/docker
    args:
      - build
      - --file=Dockerfile.chat
      - --tag=${IMAGE_URI}
      - .
images:
  - ${IMAGE_URI}
options:
  logging: CLOUD_LOGGING_ONLY
EOF

# 2. Deploy the new revision to Cloud Run.
echo ">>> Deploying to Cloud Run..."
gcloud run deploy "${SERVICE_NAME}" \
    --project="${PROJECT_ID}" \
    --region="${REGION}" \
    --image="${IMAGE_URI}" \
    --platform=managed \
    --allow-unauthenticated \
    --min-instances=0 \
    --max-instances=3 \
    --memory=512Mi \
    --cpu=1 \
    --timeout=300 \
    --concurrency=20 \
    --port=8080 \
    --set-env-vars="^|^SESSION_STORE=firestore|GOOGLE_CLOUD_PROJECT=${PROJECT_ID}|CHAT_CORS_ORIGINS=${CORS_ORIGINS}" \
    --update-secrets="ANTHROPIC_API_KEY=anthropic-api-key:latest"

# 3. Print the service URL for copy-paste into wiki/ask-chat.js.
SERVICE_URL="$(gcloud run services describe "${SERVICE_NAME}" \
    --project="${PROJECT_ID}" \
    --region="${REGION}" \
    --format='value(status.url)')"

echo
echo "=== Deployed ==="
echo "Service URL: ${SERVICE_URL}"
echo "API endpoint: ${SERVICE_URL}/api/chat"
echo
echo "Next step: update wiki/ask-chat.js API_URL constant to:"
echo "  ${SERVICE_URL}/api/chat"
echo "Then re-render Quarto and publish to gh-pages."
