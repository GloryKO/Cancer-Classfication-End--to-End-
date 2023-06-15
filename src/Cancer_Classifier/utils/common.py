import os
from box.exceptions import BoxValueError
import yaml
import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


@ensure_annotation #read yaml files
def read_yaml(path_to_yaml:Path)->ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            #logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("Empty yaml file")
    except Exception as e:
        raise e


@ensure_annotations  #creates neccesary file paths
def create_directories(path_to_directories:list,verbose=True):
    for path in path_to_directories:
        os.makedirs(path)
        if verbose:
            logger.info(f"created directory at: {path}")

@ensure_annotations
def save_json(path:Path,data:dict):
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
    logger.info(f"json saved at: {path}")