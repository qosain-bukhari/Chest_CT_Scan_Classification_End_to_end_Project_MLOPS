from Cnnclassifier.config.configuration import ConfigManager
from Cnnclassifier.components.Model_Evaluation import Evaluation, EvaluationConfig
from Cnnclassifier import logger


STAGE_NAME = "Evaluation stage"


class EvaluationPipeline:
    def __init__(self):
        pass

        # Stage 4: Model Evaluation
    def evaluation_pipeline(self):
        try:
            logger.info("Starting Model Evaluation Pipeline")
            
            # Build evaluation config
            config= ConfigManager()
            eval_config = config.get_evaluation_config()
            evaluator = Evaluation(eval_config)
            evaluator.evaluate_model()
            evaluator.save_score()
            # evaluator.log_into_mlflow()
            logger.info("Model Evaluation Pipeline completed successfully")
        except Exception as e:
            logger.exception(e)
            raise e
    
        
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = EvaluationPipeline()
        obj.evaluation_pipeline()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e

