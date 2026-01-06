import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL=os.getenv("MONGODB_URL")
print(MONGO_DB_URL)

import certifi
ca=certifi.where()
import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging


class NetworkDataExtract:
    def __init__(self):
        pass

    def csv_to_json_convertor(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records  # <--- Added return statement
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def insert_data_mongodb(self, records, database, collection):
        try:
            self.database_name = database
            self.collection_name = collection
            self.records = records
            
            # 1. Connect to Client
            self.mongo_client = pymongo.MongoClient(
    MONGO_DB_URL, 
    tls=True, 
    tlsAllowInvalidCertificates=True
)
            
            # 2. Access the Database using the client (This was the error)
            self.db = self.mongo_client[self.database_name]
            
            # 3. Access the Collection using the database object
            self.collection = self.db[self.collection_name]
            
            # 4. Insert data
            self.collection.insert_many(self.records)
            
            return len(self.records)
        except Exception as e:
            raise NetworkSecurityException(e, sys)      
if __name__=="__main__":
    FILE_PATH="Network_data\phisingData.csv"
    DATABASE="Tushar"
    Collection="NetworkData"
    networkobj=NetworkDataExtract()
    records=networkobj.csv_to_json_convertor(file_path=FILE_PATH)
    no_of_records=networkobj.insert_data_mongodb(records,DATABASE,Collection)
    