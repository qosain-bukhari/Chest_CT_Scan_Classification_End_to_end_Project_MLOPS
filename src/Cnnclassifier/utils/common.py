from Cnnclassifier import logger
import os
from ensure import ensure_annotations
from box import ConfigBox
import yaml
from typing import Any
import base64
from pathlib import Path
import json
from box.exceptions import BoxValueError

@ensure_annotations
def read_yaml(path_to_yml: Path) -> ConfigBox:
    """Reads yaml file and returns ConfigBox"""
    try:
        with open(path_to_yml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        logger.error(f"Error occurred while reading yaml file: {e}")
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Creates list of directories"""
    try:
        for path in path_to_directories:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f"Created directory at: {path}")
    except Exception as e:
        logger.error(f"Error occurred while creating directories: {e}")
        raise e

@ensure_annotations
def save_json(path: Path, data: dict):
    """Save json data"""
    try:
        with open(path, "w") as f:
            json.dump(data, f, indent=4)
        logger.info(f"json file saved at: {path}")
        return path
    except Exception as e:
        logger.error(f"Error occurred while saving json: {e}")
        raise e

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Load json data"""
    try:
        with open(path, "r") as f:
            content = json.load(f)
        logger.info(f"json file loaded successfully from: {path}")
        return ConfigBox(content)
    except Exception as e:
        logger.error(f"Error occurred while loading json: {e}")
        raise e

@ensure_annotations
def get_size_in_mb(path: Path) -> float:
    """Get size in MB"""
    try:
        size_in_bytes = os.path.getsize(path)
        size_in_mb = size_in_bytes / (1024 * 1024)
        return size_in_mb
    except Exception as e:
        logger.error(f"Error occurred while getting file size: {e}")
        raise e

@ensure_annotations
def encode_image_to_base64(image_path: Path) -> str:
    """Encode image to base64 string"""
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode('utf-8')
    except Exception as e:
        logger.error(f"Error occurred while encoding image: {e}")
        raise e

@ensure_annotations
def decode_base64_to_image(b64_string: str, output_path: Path):
    """Decode base64 string to image"""
    try:
        img_data = base64.b64decode(b64_string)
        with open(output_path, "wb") as img_file:
            img_file.write(img_data)
        return output_path
    except Exception as e:
        logger.error(f"Error occurred while decoding image: {e}")
        raise e