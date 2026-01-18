from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
from networksecurity.components.data_validation import DataValidation,DataValidationConfig
import sys
if __name__ == "__main__":
    try:
        traningpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig= DataIngestionConfig(traningpipelineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        dataiingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data ingestion completed")
        logging.info("Initiate the data validation")
        datavalidationconfig=DataValidationConfig(traningpipelineconfig)
        datavalidation=DataValidation(dataiingestionartifact,datavalidationconfig)
        data_validation_artifact=datavalidation.initiate_data_validation()
        logging.info("Data validation completed")
        print(dataiingestionartifact)
    except Exception as e:
      
        raise NetworkSecurityException(e, sys)