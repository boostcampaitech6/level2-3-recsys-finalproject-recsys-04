#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from django.conf import settings
from mlartifacts.bert4rec.model import BERT4Rec, params
from mlartifacts.bert4rec.module import *

def mlflow_model_download():
    # mlflow model download
    import mlflow
    
    mlflow.set_tracking_uri(uri=settings.MLFLOW_URL)
    
    path_category_proba = settings.PATH_CATEGORY_PROBA
    mlflow.artifacts.download_artifacts(artifact_uri="models:/ca_proba/1", dst_path=path_category_proba)
    

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GiftHubProject.settings')
    
    if settings.MODEL_DOWNLOAD_YN == "Y":
        mlflow_model_download()
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
