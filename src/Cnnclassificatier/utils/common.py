from Cnnclassificatier import logger
import os
from ensure import ensure_annotations
from box import ConfigBox
import yaml
from typing import Any
import base64
from pathlib import Path
import json

@ensure_annotations
def read_yaml(path_to_yml: Path) -> ConfigBox:
    """
    Docstring for read_yaml
    
    :param path_to_yml: Description
    :type path_to_yml: Path
    :return: Description
    :rtype: ConfigBox
    """
    with open(path_to_yml, "r") as yaml_file:
        content = yaml.safe_load(yaml_file)
    return ConfigBox(content)


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Docstring for create_directories
    
    :param path_to_directories: Description
    :type path_to_directories: list[Path]
    :return: Description
    :rtype: None
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """Save json data"""
    with open(path, "w") as f:
        json.dump(data, f, indent=4)


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Load json data"""
    with open(path, "r") as f:
        content = json.load(f)
    return ConfigBox(content)

@ensure_annotations
def get_size_in_mb(path: Path) -> float:
    """Get size in MB"""
    size_in_bytes = os.path.getsize(path)
    size_in_mb = size_in_bytes / (1024 * 1024)
    return size_in_mb

@ensure_annotations
def save_json(path: Path, data: dict):
    """Save json data"""
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    return path
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Load json data"""
    with open(path, "r") as f:
        content = json.load(f)
    return ConfigBox(content)


@ensure_annotations
def encode_image_to_base64(image_path: Path) -> str:
    """Encode image to base64 string"""
    with open(image_path, "rb") as img_file:
        b64_string = base64.b64encode(img_file.read()).decode('utf-8')
    return b64_string

@ensure_annotations
def decode_base64_to_image(b64_string: str, output_path: Path):
    """Decode base64 string to image"""
    img_data = base64.b64decode(b64_string)
    with open(output_path, "wb") as img_file:
        img_file.write(img_data)
    return output_path

