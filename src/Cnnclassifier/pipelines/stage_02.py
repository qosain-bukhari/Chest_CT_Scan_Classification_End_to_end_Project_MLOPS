from Cnnclassifier.config.configuration import ConfigManager
from Cnnclassifier.components.Prepare_base_model import PrepareBaseModel
from Cnnclassifier import logger
from Cnnclassifier.entity.config_entity import BaseModelConfig

STAGE_NAME = "Prepare base model"


class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass


    def base_model_pipeline(self):
       try:
            config=ConfigManager()
            PrepareBaseModelConfig=config.get_base_model_config()
            prepare_base_model=PrepareBaseModel(config=PrepareBaseModelConfig)
            prepare_base_model.get_base_model()
            prepare_base_model.update_base_model()
       except Exception as e:
            logger.exception(e)
            raise e


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.base_model_pipeline()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
