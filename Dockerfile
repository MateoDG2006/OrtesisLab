# Imagen única de OrtesisLab: migrate, web y worker.
# Arranque: python scripts/EntradaContenedor.py migrate|web|worker
FROM ghcr.io/astral-sh/uv:python3.14-bookworm-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends curl ca-certificates unzip \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app/apps/web:/app/apps/ortesis-plugin \
    PATH="/app/.venv/bin:$PATH" \
    REFLEX_ENV=prod

COPY pyproject.toml uv.lock ./
RUN uv sync --locked --no-dev

COPY alembic.ini ./
COPY apps ./apps
COPY core ./core
COPY scripts ./scripts

# Compila el frontend. Los valores van solo en este RUN (no quedan como ENV de la imagen).
WORKDIR /app/apps/web
RUN ORTESISLAB_DATABASE_URL=postgresql+psycopg://build:build@127.0.0.1:5432/build \
    ORTESISLAB_WORKER_DATABASE_URL=postgresql+psycopg://build:build@127.0.0.1:5432/build \
    ORTESISLAB_MIGRATOR_DATABASE_URL=postgresql+psycopg://build:build@127.0.0.1:5432/build \
    ORTESISLAB_S3_ENDPOINT=http://127.0.0.1:9000 \
    ORTESISLAB_S3_ACCESS_KEY=build \
    ORTESISLAB_S3_SECRET_KEY=build \
    ORTESISLAB_S3_BUCKET=ortesislab \
    ORTESISLAB_APP_URL=http://127.0.0.1:3000 \
    ORTESISLAB_COOKIE_SECURE=false \
    uv run --project /app reflex compile

WORKDIR /app
EXPOSE 3000

ENTRYPOINT ["uv", "run", "--project", "/app", "python", "scripts/EntradaContenedor.py"]
CMD ["web"]
