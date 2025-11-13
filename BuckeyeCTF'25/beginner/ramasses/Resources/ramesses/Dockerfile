FROM ghcr.io/astral-sh/uv:debian

COPY main.py pyproject.toml uv.lock /app/
COPY static /app/static
COPY templates /app/templates
WORKDIR /app/
RUN uv sync --locked
USER 1000
ENV PYTHONUNBUFFERED=1
CMD .venv/bin/python3 main.py
