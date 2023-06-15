import os
from box.exceptions import BoxValueError
import yaml
#import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64
from main import set_logging


@ensure_annotations #read yaml files
def read_yaml(path_to_yaml:Path)->ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            set_logging(f"yaml file: {path_to_yaml} loaded successfully")
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
            set_logging(f"created directory at: {path}")

@ensure_annotations
def save_json(path:Path,data:dict):
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
    set_logging(f"json saved at: {path}")

@ensure_annotations
def load_json(path:Path):
    with open(path, 'r') as f:
        content = json.load(f)
    set_logging(f"json loaded at: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data:Any,path:Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data,filename=path)
    set_logging(f"binary file saved at: {path}")

@ensure_annotations
def load_bin(path:Path):
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    set_logging(f"binary data loaded from{path}")
    return data

@ensure_annotations
def get_size(path:Path)->str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"

@ensure_annotations
def decodeImage(imgstring,fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()
        
@ensure_annotations
def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())