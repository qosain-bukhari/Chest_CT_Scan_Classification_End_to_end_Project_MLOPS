# src/pipelines/training_pipeline.py

from Cnnclassifier.config.configuration import ConfigManager
from Cnnclassifier.components.data_ingestion import DataIngestion
from Cnnclassifier import logger

class TrainingPipeline:
    def __init__(self):
        self.config_manager = ConfigManager()
        self.Stage = "Data Ingestion"

    def data_ingestion_pipeline(self):
        """
        Run the data ingestion pipeline
        """
        try:
            logger.info("Starting Data Ingestion Pipeline...")
            
            # Initialize data ingestion with ConfigManager
            data_ingestion = DataIngestion(self.config_manager)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            
            logger.info(f"Data Ingestion completed. ZIP file: {data_ingestion_artifact.local_data_file}, "
                        f"Extracted folder: {data_ingestion_artifact.unzip_data_dir}")
            
            return data_ingestion_artifact
        except Exception as e:
            logger.exception(f"Error in Data Ingestion Pipeline: {e}")
            raise e

if __name__ == "__main__":
    try:
        training_pipeline = TrainingPipeline()
        logger.info(f">>>> Stage: {training_pipeline.Stage}")
        artifact = training_pipeline.data_ingestion_pipeline()
        logger.info(f">>>> Stage: {training_pipeline.Stage} completed <<<<")
    except Exception as e:
        logger.exception(f"Error in Training Pipeline: {e}")
        raise e
