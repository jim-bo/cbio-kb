#!/usr/bin/env bash
# Deploy the cbio-kb chat API to Cloud Run by hand (the same steps as the
# cloud-run job in .github/workflows/chat-api.yml). Only useful if you host
# the chat API on Google Cloud; docs/hosting.md covers other hosts.
#
# Uses Cloud Build to build the image from docker/chat.Dockerfile (so we don't
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
# Usage (run from the repository root):
#   PROJECT_ID=my-project deploy/cloudrun/deploy-chat.sh
#   PROJECT_ID=... REGION=... SERVICE_NAME=... CHAT_CORS_ORIGINS=... deploy/cloudrun/deploy-chat.sh
#
# PROJECT_ID defaults to the original maintainer's project (cbioportal-python);
# set it to yours.

set -euo pipefail

PROJECT_ID="${PROJECT_ID:-cbioportal-python}"
REGION="${REGION:-us-central1}"
SERVICE_NAME="${SERVICE_NAME:-cbio-kb-api}"
REPO_NAME="${REPO_NAME:-cbio-kb}"
ANTHROPIC_SECRET="${ANTHROPIC_SECRET:-anthropic-api-key}"
IMAGE_TAG="${IMAGE_TAG:-$(git rev-parse --short HEAD 2>/dev/null || date +%s)}"
IMAGE_URI="${REGION}-docker.pkg.dev/${PROJECT_ID}/${REPO_NAME}/${SERVICE_NAME}:${IMAGE_TAG}"

# CORS origins for the chat page: the site's origin plus local dev.
CORS_ORIGINS="${CHAT_CORS_ORIGINS:-https://jim-bo.github.io,http://localhost:8080,http://127.0.0.1:8080}"

echo "=== cbio-kb chat API deploy ==="
echo "Project:  ${PROJECT_ID}"
echo "Region:   ${REGION}"
echo "Service:  ${SERVICE_NAME}"
echo "Image:    ${IMAGE_URI}"
echo "CORS:     ${CORS_ORIGINS}"
echo

# 1. Build & push the image via Cloud Build (remote build, no local Docker).
echo ">>> Submitting build to Cloud Build..."
gcloud builds submit \
    --project="${PROJECT_ID}" \
    --config=deploy/cloudrun/cloudbuild-chat.yaml \
    --substitutions="_IMAGE_URI=${IMAGE_URI}"

# 2. Deploy the new revision to Cloud Run. Sizing matches the CI deploy; the
#    image loads the reranker and query-embedding models, so 512Mi is too small.
echo ">>> Deploying to Cloud Run..."
gcloud run deploy "${SERVICE_NAME}" \
    --project="${PROJECT_ID}" \
    --region="${REGION}" \
    --image="${IMAGE_URI}" \
    --platform=managed \
    --allow-unauthenticated \
    --min-instances=0 \
    --max-instances=3 \
    --memory=2Gi \
    --cpu=2 \
    --cpu-boost \
    --timeout=300 \
    --concurrency=20 \
    --port=8080 \
    --set-env-vars="^|^SESSION_STORE=firestore|GOOGLE_CLOUD_PROJECT=${PROJECT_ID}|CHAT_CORS_ORIGINS=${CORS_ORIGINS}" \
    --update-secrets="ANTHROPIC_API_KEY=${ANTHROPIC_SECRET}:latest"

# 3. Print the service URL for the website's chat config.
SERVICE_URL="$(gcloud run services describe "${SERVICE_NAME}" \
    --project="${PROJECT_ID}" \
    --region="${REGION}" \
    --format='value(status.url)')"

echo
echo "=== Deployed ==="
echo "Service URL: ${SERVICE_URL}"
echo "API endpoint: ${SERVICE_URL}/api/chat"
echo
echo "Next step: point the website's /ask page at it, either with the"
echo "repository variable CHAT_API_URL=${SERVICE_URL}/api/chat (Website"
echo "workflow) or by editing wiki/ask-config.js."
