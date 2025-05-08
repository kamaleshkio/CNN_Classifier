from src.Chicken_Disease_classification import logger
from src.Chicken_Disease_classification.pipeline.Stage_01_Data_ingestion import DataIngestionTrainingPipeline
from src.Chicken_Disease_classification.pipeline.Stage_02_Prepare_base_model import  PrepareBaseModelTrainingPipeline
from src.Chicken_Disease_classification.pipeline.Stage_03_Training import ModelTrainingPipeline
from src.Chicken_Disease_classification.pipeline.Stage_04_Evaluation import EvaluationPipeline


STAGE_NAME = 'Data Ingestion and Training'

try:
    logger.info(f'Initializing {STAGE_NAME}')
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f'{STAGE_NAME} completed successfully')

except Exception as e:
    logger.exception(f'Error occurred during {STAGE_NAME}: {str(e)}')
    raise e

## --------------------------------------------------------------------##

STAGE_NAME = "Prepare Base Model Stage"

try:
    logger.info(f"****************************")
    logger.info(f"Starting {STAGE_NAME}")
    pipeline = PrepareBaseModelTrainingPipeline()
    pipeline.main()
    logger.info(f">>>>>>>>>>{STAGE_NAME} completed successfully<<<<<<<<<")

except Exception as e:
    logger.error(f"An error occurred during {STAGE_NAME}: {str(e)}")
    raise e

## --------------------------------------------------------------------##

STAGE_NAME = "Training Stage"
try:
    logger.info(f"****************************")
    logger.info(f"Starting {STAGE_NAME}")
    pipeline = ModelTrainingPipeline()
    pipeline.main() ###
    logger.info(f">>>>>>>>>>{STAGE_NAME} completed successfully<<<<<<<<<")

except Exception as e:
    logger.error(f"An error occurred during {STAGE_NAME}: {str(e)}")
    raise e

## --------------------------------------------------------------------##

STAGE_NAME = 'Model Evaluation Stage'

try:
    logger.info(f'Initializing {STAGE_NAME}')
    data_ingestion = EvaluationPipeline()
    data_ingestion.main()
    logger.info(f'{STAGE_NAME} completed successfully')

except Exception as e:
    logger.exception(f'Error occurred during {STAGE_NAME}: {str(e)}')
    raise e
