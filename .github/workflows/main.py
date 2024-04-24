name: Build model, push model to github registry, and deploy application

on:
    push:
        branches: [ main ]
        paths:
            - src/app/*
            - Dockerfile

    workflow_dispatch:

jobs:
    build:
        runs-on: ubuntu-latest
        steps:

            - uses: action/checkout@v2

      - name: Login to GitHub Container Registry
        uses: docker/login-action@v1
        with:
          registry: ghcr.io
          username: ${{ github.repository_owner }}
          password: ${{ secrets.GH_REGISTRY }}

      - name: Build app and push to registry
        uses: docker/build-push-action@v2
        with:
          context: ./
          tags: ghcr.io/gara2000/flask-app:latest
          push: true           