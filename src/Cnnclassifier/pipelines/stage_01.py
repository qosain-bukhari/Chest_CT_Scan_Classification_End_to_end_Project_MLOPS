from Cnnclassifier.config.configuration import ConfigManager
from Cnnclassifier.components.data_ingestion import DataIngestion
from Cnnclassifier import logger



STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def data_ingestion_pipeline(self):
        try:
            logger.info("Starting Data Ingestion Pipeline")
                    
            config = ConfigManager()
            data_ingestion = DataIngestion(config)
            artifact = data_ingestion.initiate_data_ingestion()

            logger.info(
                f"Data Ingestion completed. ZIP: {artifact.local_data_file}, "
                f"Extracted: {artifact.unzip_data_dir}"
            )
            return artifact
        except Exception as e:
            logger.exception(e)
            raise e




if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.data_ingestion_pipeline()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e