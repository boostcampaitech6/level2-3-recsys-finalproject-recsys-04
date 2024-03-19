FROM python:3.9.18
# set unbuffered mode
ENV PYTHONUNBUFFERD 1
COPY . /home/GiftHub_backend
WORKDIR /home/GiftHub_backend
# RUN sed -i "s/DEBUG = True/DEBUG = False/g" /home/ksh/level2-3-recsys-finalproject-recsys-04/GiftHub_backend/GiftHubProject/settings.py
RUN pip install -r requirements.txt \
pip install torch==1.12.1+cu113 torchvision==0.13.1+cu113 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu113
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
EXPOSE 8000