import pandas as pd
import numpy as np
from networksecurity.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact
from networksecurity.entity.config_entity import DataValidationConfig
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.constants.training_pipeline import SCHEMA_FILE_PATH
from networksecurity.logging.logger import logging 
from scipy.stats import k2_2samp
import os,sys
class DataValidation:
    def __init__(self,data_ingestion_artifact:DataIngestionArtifact,data_validation_config:DataValidationConfig):
        try:
            self.data_ingestion_config=data_ingestion_artifact
            self.data_validation_connfig=data_validation_config
            self._schema_config=read_yaml_file(SCHEMA_FILE_PATH)
        except Exception as e:
            raise NetworkSecurityException(e,sys)
