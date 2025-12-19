from Cnnclassifier.utils.common import read_yaml, create_directories
from Cnnclassifier.constants import * 
from Cnnclassifier.entity.config_entity import DataIngestionConfig
class ConfigManager:
    def __init__(self,
                 config_filepath: Path = CONFIG_FILE_PATH,
                 params_filepath: Path = PARAMS_FILE_PATH):
        # Read config and params YAML
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        
        # Create artifacts root directory
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        data_ingestion_config = DataIngestionConfig(
            root_dir=Path(config.root_dir),
            source_url=config.source_url,          # match YAML key
            local_data_file=Path(config.local_data_file),
            unzip_data_dir=Path(config.unzip_data_dir)
        )

        return data_ingestion_config