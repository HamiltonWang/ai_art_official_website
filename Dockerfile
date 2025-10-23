# Use Python 3.8.3 and Ubuntu slim as the base image
ARG BASE_IMAGE=python:3.9.18-slim
FROM --platform=linux/amd64 ${BASE_IMAGE} AS base

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    lsof \
    pkg-config \
    nano \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

FROM base as builder

ENV POETRY_VERSION=1.8.3

# start installing things with poetry
COPY poetry.lock pyproject.toml /app/
RUN pip install -U pip setuptools \
    && pip install poetry==${POETRY_VERSION}
RUN poetry config virtualenvs.create false
RUN poetry install  --no-root

# Copy the local aihedge_chatbot_prod directory to the container at /app
COPY . /app

# Set the APP_MODE build argument and default to "SpotAPI" if not set
ARG APP_MODE=PRODUCTION


# Activate the virtual environment and run the application
# CMD ["bash", "-c", "poetry run ai_art_landing"]
CMD ["poetry", "run", "ai_art_landing", "--host", "0.0.0.0", "--port", "5000"]