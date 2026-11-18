#!/bin/bash
set -euo pipefail

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "Docker is not installed. Please install Docker before running this script." >&2
    exit 1
fi

# Detect Docker Compose v2 plugin (`docker compose`) or v1 standalone (`docker-compose`)
if docker compose version &> /dev/null; then
    COMPOSE_CMD=(docker compose)
elif command -v docker-compose &> /dev/null; then
    COMPOSE_CMD=(docker-compose)
else
    echo "Docker Compose is not installed. Please install Docker Compose before running this script." >&2
    exit 1
fi

# Build and start containers in the background
"${COMPOSE_CMD[@]}" up -d --build

# Remove dangling Docker images
docker image prune -f

# Provide a message to the user
echo "Docker Compose has been executed. Your application is running in the background."
