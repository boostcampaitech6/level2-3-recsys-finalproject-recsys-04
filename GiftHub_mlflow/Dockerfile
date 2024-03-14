FROM python:3.9.18
# set unbuffered mode
ENV PYTHONUNBUFFERD 1
COPY . /home/mlflow
WORKDIR /home/mlflow
RUN pip install -r requirements.txt
CMD ["mlflow", "server", "--host", "0.0.0.0", "--port", "8010"]
EXPOSE 8010