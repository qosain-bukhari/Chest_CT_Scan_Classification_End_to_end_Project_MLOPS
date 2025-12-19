from src.Cnnclassifier import logger
from Cnnclassifier.pipelines.Training_pipeline import TrainingPipeline

try:
        # Initialize the training pipeline
        training_pipeline = TrainingPipeline()
        
        # Log the stage
        logger.info(f">>>> Stage: {training_pipeline.Stage} is starting <<<<<<")
        
        # Run the data ingestion pipeline
        artifact = training_pipeline.data_ingestion_pipeline()
        
        # Log completion
        logger.info(f">>>> Stage: {training_pipeline.Stage} completed <<<<")
        
        # Print artifact paths (optional)
        print(f"ZIP file path: {artifact.local_data_file}")
        print(f"Extracted data path: {artifact.unzip_data_dir}")
except Exception as e:
        logger.exception(f"Error in Training Pipeline: {e}")
        raise e