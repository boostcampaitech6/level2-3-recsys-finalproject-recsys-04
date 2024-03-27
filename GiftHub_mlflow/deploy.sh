#!/bin/bash
VERSION=1.0.1
cd /home/ksh/camp/level2-3-recsys-finalproject-recsys-04/GiftHub_mlflow
docker build --no-cache . --tag mlflow:${VERSION}
docker stop mlflow
docker rm mlflow
docker run -dit -v /home/ksh/camp/level2-3-recsys-finalproject-recsys-04/GiftHub_mlflow:/home/mlflow -p 8010:8010 --name mlflow mlflow:${VERSION}
