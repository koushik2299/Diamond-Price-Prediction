import os
import pandas as pd
import sys

from sklearn.impute import SimpleImputer ## HAndling Missing Values
from sklearn.preprocessing import StandardScaler # HAndling Feature Scaling
from sklearn.preprocessing import OrdinalEncoder # Ordinal Encoding
## pipelines
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

sys.path.append('/Users/praneeth/Desktop/Koushik/Diamond_Price_Prediction/Diamond-Price-Prediction')

from src.logger import logging
from src.exception import CustomException
from src.components.data_ingestion import DataIngestion

if __name__ == 'main':
    obj = DataIngestion()
    train_data_path,test_data_path = obj.init_data_ingestion()
    print(train_data_path,test_data_path)