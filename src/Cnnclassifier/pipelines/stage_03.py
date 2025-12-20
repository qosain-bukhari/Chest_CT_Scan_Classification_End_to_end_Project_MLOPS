from Cnnclassifier.config.configuration import ConfigManager
from Cnnclassifier.components.model_training import ModelTrainingConfig, Training
from Cnnclassifier import logger




STAGE_NAME = "model_Training"

class ModelTrainingPipeline:
    def __init__(self):
        pass
    # Stage 3: Model Training
    def model_training_pipeline(self):
        try:
            config = ConfigManager()
            training_config = config.get_training_config()
            training = Training(config=training_config)
            training.get_base_model()
            training.train_valid_generator()
            training.train()
            
        except Exception as e:
            raise e
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.model_training_pipeline()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e