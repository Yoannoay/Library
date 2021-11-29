#!/bin/bash

echo "Deploy stage... now!"


scp docker-compose.yaml jenkins@swarm-manager:/home/jenkins/docker-compose.yaml

ssh jenkins@swarm-manager \
    DOCKER_HUB_CREDS_USR=$DOCKER_HUB_CREDS_USR \
    DATABASE_URI=$DATABASE_URI \
    CREATE_SCHEMA=true \
    docker stack deploy --compose-file docker-compose.yaml todo-app
