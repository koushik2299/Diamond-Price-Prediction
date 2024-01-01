import os 
import src
from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass

import pandas as pd
import sklearn.model_selection import train_test_split

@dataclass
class DataIngestionconfig:
    train_data_path:str = os.path.join('artifacts','train.csv')
    test_data_path:str = os.path.join('artifacts','test.csv')
    raw_data_path:str = os.path.join('artifacts','raw.csv')
    
