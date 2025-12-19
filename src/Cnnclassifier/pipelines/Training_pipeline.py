# src/pipelines/training_pipeline.py

from Cnnclassifier.config.configuration import ConfigManager
from Cnnclassifier.components.data_ingestion import DataIngestion
from Cnnclassifier.components.Prepare_base_model import PrepareBaseModel
from Cnnclassifier.entity.config_entity import BaseModelConfig
from Cnnclassifier import logger

class TrainingPipeline:
    def __init__(self):
        self.config_manager = ConfigManager()
        self.Stage = "Data Ingestion & Base Model Training"

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

    def base_model_training_pipeline(self):
        """
        Run base model preparation and training pipeline
        """
        try:
            logger.info("Starting Base Model Training Pipeline...")

            # Get configuration
            base_model_config: BaseModelConfig = self.config_manager.get_base_model_config()

            # Prepare base model
            prepare_base_model = PrepareBaseModel(config=base_model_config)
            
            # Load or create base model
            base_model = prepare_base_model.get_base_model()

            # Update base model with classification head
            updated_model = prepare_base_model.update_base_model()

            # Save updated base model
            prepare_base_model.save_model(
                model=updated_model,
                path=base_model_config.updated_base_model_path
            )

            logger.info(f"Base Model Training Pipeline completed successfully.")
            return updated_model

        except Exception as e:
            logger.exception(f"Error in Base Model Training Pipeline: {e}")
            raise e


if __name__ == "__main__":
    try:
        training_pipeline = TrainingPipeline()

        # Stage 1: Data Ingestion
        logger.info(f">>>> Stage: Data Ingestion started <<<<")
        artifact = training_pipeline.data_ingestion_pipeline()
        logger.info(f">>>> Stage: Data Ingestion completed <<<<\n")

        # Stage 2: Base Model Training
        logger.info(f">>>> Stage: Base Model Training started <<<<")
        updated_model = training_pipeline.base_model_training_pipeline()
        logger.info(f">>>> Stage: Base Model Training completed <<<<")

    except Exception as e:
        logger.exception(f"Error in Training Pipeline: {e}")
        raise e
