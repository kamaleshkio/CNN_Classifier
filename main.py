from src.Chicken_Disease_classification import logger
from src.Chicken_Disease_classification.pipeline.Stage_01_Data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = 'Data Ingestion and Training'

try:
    logger.info(f'Initializing {STAGE_NAME}')
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f'{STAGE_NAME} completed successfully')

except Exception as e:
    logger.exception(f'Error occurred during {STAGE_NAME}: {str(e)}')
    raise e


