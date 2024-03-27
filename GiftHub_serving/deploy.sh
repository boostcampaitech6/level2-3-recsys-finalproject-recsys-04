#!/bin/bash
cd /home/ksh/camp/level2-3-recsys-finalproject-recsys-04/GiftHub_serving
VERSION=1.0.1
docker build --no-cache . --tag fastapi:${VERSION}
docker stop fastapi
docker rm fastapi
docker run --gpus all -dit -v /home/ksh/camp/level2-3-recsys-finalproject-recsys-04/GiftHub_serving:/home/GiftHub_serving -p 8011:8011 --name fastapi fastapi:${VERSION}