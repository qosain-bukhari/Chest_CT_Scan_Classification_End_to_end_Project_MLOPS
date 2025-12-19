from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    """
    Data class to store configuration for data ingestion
    """
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_data_dir: Path

@dataclass(frozen=True)
class BaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_classes: int
    params_weights: str
    params_include_top: bool