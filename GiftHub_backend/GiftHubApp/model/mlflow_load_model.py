import mlflow
from django.conf import settings

model_ca_proba = mlflow.pyfunc.load_model(settings.PATH_CATEGORY_PROBA)