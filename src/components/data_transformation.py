from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler 
from sklearn.preprocessing import OrdinalEncoder

from sklearn.pipelines import Pipeline
from sklearn.compose import ColumnTransformer
import numpy as np
import pandas as pd

from src.exception import CustomException
from src.logger import logging 
import sys,os
from dataclasses import dataclass

@dataclass
class DataTransformationConfig:
    preprocess_obj_file_path = os.path.join('artifacts','preprocessor.pkl')

class DataTransformation:

    def __init__(self):
            self.data_transformation_config = DataTransformationConfig()

    def function_data_preprocessing(self):
        try:
            logging.info("Data PreProcessing Methods")

            categorical_cols = ['cut','color','clarity']
            numerical_cols = ['carat','depth','table','x','y','z']

            cut_categories = ['Fair','Good','Very Good','Premium','Ideal']
            color_categories = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
            clarity_categories = ['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']

            num_pipeline = Pipeline(
                steps = [
                    ('Imputer',SimpleImputer(strategy='median')),
                    ('Scaler',StandardScaler())
                ]
            )

            cat_pipeline = Pipeline(
                steps = [
                    ('Imputer',SimpleImputer(strategy='most_frequent')),
                    ('Ordinal Encoder',OrdinalEncoder(categories=categorical_cols))

                ]
            )

            logging.info('Pipeline Started')

            preprocessor = ColumnTransformer([
                ('cat_pipeline',cat_pipeline,categorical_cols,)
                ('num_pipeline',num_pipeline,num_pipeline)
            ])

            logging.info('Pipeline Completed')

            logging.info('Data Preprocessing Completed')
            return(preprocessor)


        except Exception as e:
            logging.info('Problem In Data Transformation')
            raise CustomException(e,sys)

    def init_data_transformation(self,train_data_path,test_data_path):
        try:
            train_df = pd.read_csv(train_data_path)
            test_df = pd.read_csv(test_data_path)
            
            file = self.function_data_preprocessing()

            target_column = "price"
            drop_columns = [target_column,"id"]

            input_train_feature_df = train_df.drop(drop_columns,axis=1,inplace=False)
            input_train_target_df = train_df[target_column]

            input_test_feature_df = test_df.drop(drop_columns,axis=1,inplace=False)
            input_test_target_df = test_df[target_column]

            logging.info("PreProcessing Steps are being applied to train and test data")
            input_train_feature_df=file.fit_transform(input_train_feature_df)
            input_test_feature_df = file.fit(input_test_feature_df)

            



        
        except Exception as e:
            logging.info("Exception occured as initiating Data Transformation")
            raise CustomException(e,sys)

