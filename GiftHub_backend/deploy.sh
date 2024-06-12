#!/bin/bash
cd /home/ksh/camp/level2-3-recsys-finalproject-recsys-04/GiftHub_backend
VERSION=1.2.0
docker build --no-cache . --tag django:${VERSION}
docker stop django
docker rm django
docker run -dit -p 8000:8000 --name django django:${VERSION}