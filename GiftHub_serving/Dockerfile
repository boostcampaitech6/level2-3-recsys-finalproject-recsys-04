FROM python:3.9.18
# set unbuffered mode
ENV PYTHONUNBUFFERD 1
COPY . /home/GiftHub_serving
WORKDIR /home/GiftHub_serving
# RUN sed -i "s/DEBUG = True/DEBUG = False/g" /home/ksh/level2-3-recsys-finalproject-recsys-04/GiftHub_backend/GiftHubProject/settings.py
RUN pip install -r requirements.txt \
pip install torch==1.12.1+cu113 --extra-index-url https://download.pytorch.org/whl/cu113
CMD ["python", "main.py"]
EXPOSE 8011