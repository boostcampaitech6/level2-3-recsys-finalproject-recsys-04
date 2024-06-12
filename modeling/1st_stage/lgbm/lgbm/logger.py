import os
import random
import time

import numpy as np


# random seed로 동일한 실험결과 얻음 -> 실험할 때 쓰임
def set_seeds(seed: int = 42):
    os.environ["PYTHONHASHSEED"] = str(seed)
    random.seed(seed)
    np.random.seed(seed)


def get_logger(logger_conf: dict):
    import logging
    import logging.config

    logging.config.dictConfig(logger_conf)
    logger = logging.getLogger()
    return logger

def get_data_info(logger, df, train_data, args):
    columns = ''
    for col in df.columns:
        columns += col + ', '
    cat_columns = ''
    for col in args.cat_cols:
        cat_columns += col + ', '
    con_columns = ''
    for col in args.con_cols:
        con_columns += col + ', '
    
    logger.info(f"  📋 Dataset Information")
    logger.info(f"      Model : {args.model}")
    logger.info(f"      Column : {columns}")
    logger.info(f"      Column Length : {len(df.columns)}")
    logger.info(f"      Cat Column : {cat_columns}")
    logger.info(f"      Con Column : {con_columns}")
    logger.info(f"      Train Data Total : {len(train_data.values)}")

def get_save_time():
    
    now = time.localtime()
    now_date = time.strftime('%m%d', now)
    now_hour = time.strftime('%X', now)
    save_time = now_date + '_' + now_hour.replace(':', '')
    
    return save_time

logging_conf = {  # only used when 'user_wandb==False'
    "version": 1,
    "formatters": {
        "basic": {"format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"}
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "basic",
            "stream": "ext://sys.stdout",
        },
        "file_handler": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "basic",
            "filename": "run.log",
        },
    },
    "root": {"level": "INFO", "handlers": ["console", "file_handler"]},
}