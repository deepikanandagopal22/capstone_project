#!/bin/bash

DOCKER_USER="deepikanandagopal"
APP_NAME="ecommerce-app"

TAG=${1:-latest}


docker tag $DOCKER_USER/$APP_NAME-frontend:latest $DOCKER_USER/$APP_NAME-frontend:$TAG
docker push $DOCKER_USER/$APP_NAME-frontend:$TAG

docker tag $DOCKER_USER/$APP_NAME-backend:latest $DOCKER_USER/$APP_NAME-backend:$TAG
docker push $DOCKER_USER/$APP_NAME-backend:$TAG

echo "Images pushed to Docker Hub with tag: $TAG"


docker-compose up -d

