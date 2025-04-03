from src.Chicken_Disease_classification.constants import *
from Chicken_Disease_classification.utils.common import read_yaml, create_directory 
from pathlib import Path
from Chicken_Disease_classification.entity.config_entity import DataIngestionConfig
class ConfigurationManager:
    def __init__(
            self,
            config_file_path = CONFIG_FILE_PATH,
            params_file_path = PARAMS_FILE_PATH,):

            self.config = read_yaml(config_file_path)
            self.params = read_yaml(params_file_path)

            create_directory([self.config.artifacts_root])

    def get_ingetsion_config(self) -> DataIngestionConfig:
          config = self.config.data_ingestion

          create_directory([config.root_dir])

          data_ingestion_config = DataIngestionConfig(
                root_dir=config.root_dir,
                source_URL=config.source_URL,
                local_data_file=Path(config.local_data_file),
                unzip_dir=Path(config.unzip_dir),
          )
          return data_ingestion_config