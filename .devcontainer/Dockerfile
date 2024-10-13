FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

RUN apt-get update -y && \
    apt-get install \
    curl \
    git \
    bash-completion -y && \
    pip install -U pip && \
    pip install poetry==1.8.3 && \
    rm -rf /var/lib/apt/lists/*
