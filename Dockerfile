FROM python:3.12-slim

WORKDIR /app

# PyTorch CPU only (keeps image small)
RUN pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu

# Install the package with server extras
COPY pyproject.toml README.md ./
COPY src/ ./src/
RUN pip install --no-cache-dir ".[server]"

# Runtime artifacts (mounted or baked in)
COPY data/index_dir /app/data/index_dir
COPY data/pmid_to_pmcid.csv /app/data/pmid_to_pmcid.csv

EXPOSE 8123
ENV INDEX_DIR=/app/data/index_dir
ENV PMID_MAPPING_CSV=/app/data/pmid_to_pmcid.csv

CMD ["cbio-kb", "serve", "--host", "0.0.0.0", "--port", "8123"]
