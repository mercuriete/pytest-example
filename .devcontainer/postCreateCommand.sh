#!/bin/bash
python -m venv .venv && \
source .venv/bin/activate && \
poetry install && \
echo "" && \
python --version && \
pip --version && \
poetry --version && \
cat README.md
