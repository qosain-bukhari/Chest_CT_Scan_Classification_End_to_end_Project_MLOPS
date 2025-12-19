from src.Cnnclassifier import logger
from Cnnclassifier.pipelines.Training_pipeline import TrainingPipeline

try:
    # Initialize the training pipeline
    training_pipeline = TrainingPipeline()
    
    # # Stage 1: Data Ingestion
    # training_pipeline.Stage = "Data Ingestion"  # set stage name
    # logger.info(f">>>> Stage: {training_pipeline.Stage} is starting <<<<<<")
    # artifact = training_pipeline.data_ingestion_pipeline()
    # logger.info(f">>>> Stage: {training_pipeline.Stage} completed <<<<")

    # Stage 2: Base Model Trainin
    training_pipeline.Stage = "Base Model Training"  # update stage name
    logger.info(f">>>> Stage: {training_pipeline.Stage} is starting <<<<<<")
    updated_model = training_pipeline.base_model_pipeline()
    logger.info(f">>>> Stage: {training_pipeline.Stage} completed <<<<")

    # Stage 3: Model Training
    training_pipeline.Stage = "Model Training"  # update stage name
    logger.info(f">>>> Stage: {training_pipeline.Stage} is starting <<<<<<")
    training_pipeline.model_training_pipeline()
    logger.info(f">>>> Stage: {training_pipeline.Stage} completed <<<<")
except Exception as e:
    logger.exception(f"Error in Training Pipeline: {e}")
    raise e
