FROM python:3.11-slim

WORKDIR /app

# Optional but safe for many Python builds
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install deps first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files (src/, web/, app.py, data/, etc.)
COPY . .

# Container listens on 8080 (because your workflow maps 8080:8080)
EXPOSE 8080

# Start FastAPI on port 8080
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
