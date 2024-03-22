FROM nvidia/cuda:11.4.3-runtime-ubuntu20.04
RUN apt-get update
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get install -y python3.9
RUN apt-get install -y python3-pip
RUN pip install --upgrade pip
RUN apt-get install pkg-config
RUN apt-get install libmariadb-dev -y
# set unbuffered mode
COPY . /home/GiftHub_backend
WORKDIR /home/GiftHub_backend
# RUN sed -i "s/DEBUG = True/DEBUG = False/g" /home/ksh/level2-3-recsys-finalproject-recsys-04/GiftHub_backend/GiftHubProject/settings.py
RUN pip install -r requirements.txt \
pip install torch==1.12.1+cu113 torchvision==0.13.1+cu113 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu113
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
EXPOSE 8000