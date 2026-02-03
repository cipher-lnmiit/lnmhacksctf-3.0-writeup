FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=4069

# Install tiny extras (curl for healthcheck). Keep image small.
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Create a non-root user to run the app
RUN adduser --disabled-password --gecos "" appuser

# Copy requirements first for better caching, install gunicorn too
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt gunicorn

# Copy application code and assets
COPY . /app
RUN chown -R appuser:appuser /app

USER appuser

EXPOSE 4069

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s \
  CMD curl -f http://127.0.0.1:4069/messages || exit 1

# Run with gunicorn; bind to the expected port and interface
CMD ["gunicorn", "--bind", "0.0.0.0:4069", "--workers", "2", "app:app"]
