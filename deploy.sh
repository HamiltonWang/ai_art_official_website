#!/bin/bash

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "Docker is not installed. Please install Docker before running this script."
    exit 1
fi

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo "Docker Compose is not installed. Please install Docker Compose before running this script."
    exit 1
fi

# Run Docker Compose
docker-compose up  --build

# Remove orphaned Docker images
docker image prune -f

# Provide a message to the user
echo "Docker Compose has been executed. Your application is running in the background."
