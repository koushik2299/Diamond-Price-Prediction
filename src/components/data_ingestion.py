import os 
from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass

import pandas as pd
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionconfig:
    train_data_path:str = os.path.join('artifacts','train.csv')
    test_data_path:str = os.path.join('artifacts','test.csv')
    raw_data_path:str = os.path.join('artifacts','raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionconfig()

    def initiate_data_ingestion(self):
        logging.info('Data Ingestion Started')

        try:
            df = pd.read_csv(os.path.join('notebooks','data','gemstone.csv'))
            logging.info('Data Frame read as Pandas DataFrame')

            os.mkdirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info('Raw Data is exported')

            train_set,test_set = train_test_split(df,test_size=0.3,random_state=24)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info('Train and Test Data are generated')

            return(self.ingestion_config.train_data_path,self.ingestion_config.test_data_path)


        except Exception as e:
            logging.info('Exception Occured at Data Ingestion Stage')
            raise CustomException(e,sys)   

