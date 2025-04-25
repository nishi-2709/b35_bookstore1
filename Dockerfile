FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    && rm -rf /var/lib/apt/lists/*

# Create a non-root user first
RUN adduser --disabled-password --gecos '' appuser

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY --chown=appuser:appuser . .

# Set proper permissions
RUN chown -R appuser:appuser /app
RUN chmod -R 755 /app

# Switch to non-root user
USER appuser

EXPOSE 8000

CMD ["gunicorn", "bookstore.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "2", "--timeout", "120"] 