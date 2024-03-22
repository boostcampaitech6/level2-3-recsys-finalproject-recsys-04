#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from django.conf import settings

sys.path.append(os.path.join(os.path.join(os.path.abspath(os.path.dirname(__file__)), "mlartifacts"), "BERT4Rec"))
sys.path.append(os.path.join(os.path.join(os.path.abspath(os.path.dirname(__file__)), "mlartifacts"), "EASE"))
sys.path.append(os.path.join(os.path.join(os.path.abspath(os.path.dirname(__file__)), "mlartifacts"), "lightgcn"))

def mlflow_model_download():
    # mlflow model download
    import mlflow
    
    mlflow.artifacts.download_artifacts(artifact_uri=settings.LGBM_VER, dst_path=settings.LGBM_PATH)
    mlflow.artifacts.download_artifacts(artifact_uri=settings.BERT4REC_VER, dst_path=settings.BERT4REC_PATH)
    mlflow.artifacts.download_artifacts(artifact_uri=settings.EASE_VER, dst_path=settings.EASE_PATH)
    mlflow.artifacts.download_artifacts(artifact_uri=settings.LGCN_VER, dst_path=settings.LGCN_PATH)
    

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GiftHubProject.settings')
    
    if settings.MODEL_DOWNLOAD_YN == "Y":
        mlflow_model_download()
    print(f"Device Setting = {settings.DEVICE}")
    
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
