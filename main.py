from Cnnclassifier.pipelines import stage_01,stage_02,stage_03,stage_04
from src.Cnnclassifier import logger
from Cnnclassifier.pipelines.stage_01 import DataIngestionTrainingPipeline
from Cnnclassifier.pipelines.stage_02 import PrepareBaseModelTrainingPipeline
from Cnnclassifier.pipelines.stage_03 import ModelTrainingPipeline
from Cnnclassifier.pipelines.stage_04 import EvaluationPipeline
import dagshub
dagshub.init(
    repo_owner='qosain-bukhari', 
    repo_name='Chest_CT_Scan_Classification_End_to_end_Project_MLOPS', 
    mlflow=True
)

  



STAGE_NAME = "Prepare base model"
try:
    logger.info(f">>>>>> stage {stage_02.STAGE_NAME} started <<<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.base_model_pipeline()
    logger.info(f">>>>>> stage {stage_02.STAGE_NAME} completed <<<<<< \n\nx==========x")
except Exception as e:
    logger.exception(f"Error in Training Pipeline: {e}")
    raise e 


STAGE_NAME = "Training"
try:
    logger.info(f">>>>>> stage {stage_03.STAGE_NAME} started <<<<<<")
    obj = ModelTrainingPipeline()
    obj.model_training_pipeline()
    logger.info(f">>>>>> stage {stage_03.STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(f"Error in Training Pipeline: {e}")
    raise e


STAGE_NAME = "Evaluation stage"
try:
    logger.info(f">>>>>> stage {stage_04.STAGE_NAME} started <<<<<<")
    obj = EvaluationPipeline()
    obj.evaluation_pipeline()
    logger.info(f">>>>>> stage {stage_04.STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(f"Error in Training Pipeline: {e}")
    raise e
