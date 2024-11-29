#!/bin/bash

DOCKER_USER="deepikanandagopal"
APP_NAME="ecommerce-app"


docker build -f Dockerfile-frontend -t $DOCKER_USER/$APP_NAME-frontend:latest .
docker build -f Dockerfile -t $DOCKER_USER/$APP_NAME-backend:latest .

echo "Docker images built successfully."

