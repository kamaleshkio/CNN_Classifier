from Chicken_Disease_classification.config.configuration import ConfigurationManager
from Chicken_Disease_classification.components.data_ingestion import DataIngestion
from Chicken_Disease_classification import logger

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_ingetsion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.download_file()

        data_ingestion.extract_zip_file()
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\n==================")
    
    except Exception as e:
        logger.error(f"An error occurred in stage {STAGE_NAME}: {e}")
        raise e