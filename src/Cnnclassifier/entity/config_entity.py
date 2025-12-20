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


@dataclass(frozen=True)
class ModelTrainingConfig:
    """
    Configuration for model training
    """
    root_dir: Path
    trained_model_path: Path
    updated_base_model_path: Path
    training_data: Path
    params_epochs: int
    params_batch_size: int
    params_image_size: list
    params_is_augmentation: bool
    params_learning_rate: float

from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class EvaluationConfig:
    path_model: Path
    training_data: Path
    all_params: dict
    mlflow_url:str
    params_image_size: list
    params_batch_size: int