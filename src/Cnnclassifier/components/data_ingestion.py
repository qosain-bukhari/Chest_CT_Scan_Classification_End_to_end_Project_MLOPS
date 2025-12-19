# src/components/data_ingestion.py

import gdown
import zipfile
import os
from pathlib import Path
from Cnnclassifier.config.configuration import ConfigManager
from Cnnclassifier.entity.config_entity import DataIngestionConfig
from Cnnclassifier import logger

class DataIngestion:
    def __init__(self, config: ConfigManager):
        # Get DataIngestionConfig object from ConfigManager
        self.config = config.get_data_ingestion_config()

    def download_data(self) -> Path:
        """Download the ZIP file from Google Drive"""
        try:
            os.makedirs(self.config.root_dir, exist_ok=True)
            logger.info(f"Downloading data from: {self.config.source_url}")
            gdown.download(self.config.source_url, str(self.config.local_data_file), quiet=False)
            logger.info(f"Data downloaded successfully at: {self.config.local_data_file}")
            return self.config.local_data_file
        except Exception as e:
            logger.exception(f"Error occurred while downloading data: {e}")
            raise e

    def unzip_data(self, zip_file_path: Path) -> Path:
        """Unzip the downloaded file"""
        try:
            logger.info(f"Extracting ZIP file: {zip_file_path}")
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(self.config.unzip_data_dir)
            logger.info(f"Data extracted successfully at: {self.config.unzip_data_dir}")
            return self.config.unzip_data_dir
        except Exception as e:
            logger.exception(f"Error occurred while extracting ZIP file: {e}")
            raise e

    def initiate_data_ingestion(self) -> DataIngestionConfig:
        """Run download and unzip sequentially and return full DataIngestionConfig"""
        zip_file = self.download_data()
        unzip_dir = self.unzip_data(zip_file)
        
        # Return a full DataIngestionConfig object
        return DataIngestionConfig(
            root_dir=self.config.root_dir,
            source_url=self.config.source_url,
            local_data_file=zip_file,
            unzip_data_dir=unzip_dir
        )
