from src.Cnnclassifier import logger
from Cnnclassifier.pipelines.Training_pipeline import TrainingPipeline

try:
    # Initialize the training pipeline
    training_pipeline = TrainingPipeline()
    
    # =======================
    # Stage 1: Data Ingestion
    # =======================
    logger.info(f">>>> Stage: {training_pipeline.Stage} is starting <<<<<<")
    artifact = training_pipeline.data_ingestion_pipeline()
    logger.info(f">>>> Stage: {training_pipeline.Stage} completed <<<<")
    
    # Optional: Print artifact paths
    print(f"ZIP file path: {artifact.local_data_file}")
    print(f"Extracted data path: {artifact.unzip_data_dir}")

    # =======================
    # Stage 2: Base Model Training
    # =======================
    training_pipeline.Stage = "Base Model Training"  # update stage name
    logger.info(f">>>> Stage: {training_pipeline.Stage} is starting <<<<<<")
    updated_model = training_pipeline.base_model_training_pipeline()
    logger.info(f">>>> Stage: {training_pipeline.Stage} completed <<<<")

    # Optional: Print path of updated base model
    print(f"Updated base model saved at: {training_pipeline.config_manager.get_base_model_config().updated_base_model_path}")

except Exception as e:
    logger.exception(f"Error in Training Pipeline: {e}")
    raise e
