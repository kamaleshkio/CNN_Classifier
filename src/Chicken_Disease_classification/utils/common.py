import os
from box.exceptions import BoxValueError
import yaml
from Chicken_Disease_classification import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Read a YAML file into a config_box."

    args: 
        path_to_yaml (Path): Path to the YAML file to read.

    returns:
        config_box: A config_box object containing the contents of the YAML file.

    """

    try:
        with open(path_to_yaml, 'r') as file:
            yaml_data = yaml.safe_load(file)
            logger.info(f"Successfully read YAML file '{path_to_yaml}'.")
            return ConfigBox(yaml_data)
        
    except BoxValueError:
        raise ValueError("yaml file '{path_to_yaml}' is empty.")
    
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directory(directory_path: list, verbose=True):
        
    """
    Create a directory if it doesn't exist.

    args:
        directory_path (Path): Path to the directory to create.
        ignore_log (bool): Flag to ignore logging messages.
    """

    for path in directory_path:
        os.makedirs(path, exist_ok=True)
    if verbose:
        logger.info(f"Created directory at '{path}'.")

    
@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Save a dictionary to a JSON file.
    Args:
        path (Path): Path to the JSON file to save.
        data (dict): Dictionary to save.
        
    """

    with open(path, 'w') as file:
        json.dump(data, file, indent=4)

    logger.info(f"Successfully saved JSON file '{path}'.")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    load a JSON file into a config_box.

    args:
            path (Path): Path to the JSON file to load.

    returns:
            config_box: A config_box object containing the contents of the JSON file.
        
    """

    with open(path) as file:
        content = json.load(file)

    logger.info(f"Successfully loaded JSON file '{path}'.")
    return ConfigBox(content)
    

@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    save data to a binary file.

    args:
    data (Any): Data to save as binary format.
    path (Path): Path to the binary file to save.

    """

    joblib.dump(value=data, filename=path)
    logger.info(f"Successfully saved binary file '{path}'.") 


@ensure_annotations
def load_bin(path: Path) -> Any:
        
    """
    load data from a binary file.
        
    Args:
        path (Path): Path to the binary file to load.

    returns:
        Any: Loaded data from the binary file.
        
    """

    data = joblib.load(path)
    logger.info(f"Successfully loaded binary file '{path}'.")
    return data
    
@ensure_annotations
def get_size(path: Path) -> str:
    """
    get size in KB.
        
    Args:
        
    path (Path): Path to the file.

    returns:
        str: Size of the file in KB.
    """

    size_in_kb = round(os.path.getsize(path) / 1024, 2)
    return f"~{size_in_kb} KB"
    

def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()
        logger.info(f"Successfully decoded image '{fileName}'.")

    
def encodeImageIntoBase64(cropedImagePath):
    with open(cropedImagePath, 'rb') as image_file:
        logger.info(f"Successfully encoded image into base64 '{cropedImagePath}'.")        
        return base64.base64encode(image_file.read())
        
            