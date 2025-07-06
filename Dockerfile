# Google Cloud Run Deployment Guide for AirPreQ

## Prerequisites
- Google Cloud account: https://cloud.google.com/
- Google Cloud CLI installed
- Docker installed (we'll create a Dockerfile)
- Credit card (required, but free tier available)

## Step 1: Create Dockerfile

<function_calls>
<invoke name="create_file">
<parameter name="content"># Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first (for better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create non-root user for security
RUN useradd --create-home --shell /bin/bash app && chown -R app:app /app
USER app

# Expose port
EXPOSE 8080

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
