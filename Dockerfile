# Syntax für Dockerfile
# Verwende ein offizielles Python-Basisimage
FROM python:3.12-slim

# Setze Umgebungsvariablen für Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Arbeitsverzeichnis im Container setzen.
WORKDIR /app

# Kopiere die Anforderungen in den Container
COPY requirements.txt .

# Installiere die Abhängigkeiten
RUN pip install --no-cache-dir -r requirements.txt

# Kopiere den Quellcode in den Container
COPY . .

# Exponiere den Port 8081
EXPOSE 8081

# Verwende Gunicorn, um die App zu starten, und setze den Port auf 8081
CMD gunicorn 'main:app' --bind=0.0.0.0:8081

LABEL org.opencontainers.image.source https://github.com/nathanielconstructive/zu-bbbearbeiten-stateless