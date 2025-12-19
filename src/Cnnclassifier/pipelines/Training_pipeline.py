from Cnnclassifier.config.configuration import ConfigManager
from Cnnclassifier.components.data_ingestion import DataIngestion
from Cnnclassifier.components.Prepare_base_model import PrepareBaseModel
from Cnnclassifier.components.model_training import Training
from Cnnclassifier.entity.config_entity import BaseModelConfig
from Cnnclassifier import logger


class TrainingPipeline:
    def __init__(self):
        self.config_manager = ConfigManager()

  
    # Stage 1: Data Ingestion

    def data_ingestion_pipeline(self):
        try:
            logger.info("Starting Data Ingestion Pipeline")

            data_ingestion = DataIngestion(self.config_manager)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

            logger.info(
                f"Data Ingestion completed. ZIP: {data_ingestion_artifact.local_data_file}, "
                f"Extracted: {data_ingestion_artifact.unzip_data_dir}"
            )

            return data_ingestion_artifact

        except Exception as e:
            logger.exception(e)
            raise e

    # Stage 2: Base Model

    def base_model_pipeline(self):
        try:
            logger.info("Starting Base Model Pipeline")

            base_model_config: BaseModelConfig = self.config_manager.get_base_model_config()

            prepare_base_model = PrepareBaseModel(config=base_model_config)

            prepare_base_model.get_base_model()
            updated_model = prepare_base_model.update_base_model()

            logger.info("Base Model Pipeline completed successfully")
            return updated_model

        except Exception as e:
            logger.exception(e)
            raise e
    # Stage 3: Model Training

    def model_training_pipeline(self):
        try:
            logger.info("Starting Model Training Pipeline")

            training_config = self.config_manager.get_training_config()

            trainer = Training(config=training_config)

            trainer.get_base_model()
            trainer.train_valid_generator()
            trainer.train()

            logger.info("Model Training Pipeline completed successfully")

        except Exception as e:
            logger.exception(e)
            raise e


# =========================
# Pipeline Runner
# =========================
if __name__ == "__main__":
    try:
        pipeline = TrainingPipeline()

        logger.info(">>>> Stage 1: Data Ingestion started <<<<")
        pipeline.data_ingestion_pipeline()
        logger.info(">>>> Stage 1: Data Ingestion completed <<<<\n")

        logger.info(">>>> Stage 2: Base Model Preparation started <<<<")
        pipeline.base_model_pipeline()
        logger.info(">>>> Stage 2: Base Model Preparation completed <<<<\n")

        logger.info(">>>> Stage 3: Model Training started <<<<")
        pipeline.model_training_pipeline()
        logger.info(">>>> Stage 3: Model Training completed <<<<")

    except Exception as e:
        logger.exception(e)
        raise e
