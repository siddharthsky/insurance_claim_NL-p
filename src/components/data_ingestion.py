import os
import datetime as dt
import numpy as np
import pandas as pd
from dataclasses import dataclass

from sklearn.model_selection import train_test_split

#Local Components
from src.components.data_viz import VizStore
from src.components.data_transformation import DataTransformation

@dataclass
class DataIngestionConfig():
    # Configuration for final file paths for train, test and raw_data
    artifact_time = "Run " + str(dt.datetime.now().strftime('%m_%d_%Y_%H_%M'))
    train_data_path = os.path.join((f"artifacts\T+{artifact_time}"),"train.csv")
    test_data_path = os.path.join ((f"artifacts\T+{artifact_time}"),"test.csv")
    raw_data_path = os.path.join((f"artifacts\T+{artifact_time}"),"data.csv")
    print(raw_data_path)

class DataIngestion:
    def __init__(self,raw_file):
        self.ingestion_config = DataIngestionConfig()
        self.raw_file = raw_file
        self.sub = False

    def initialize_data_ingestion(self):
        try:
            df=pd.read_excel("notebooks\Dataset_Public_mini.xlsx")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True) # type: ignore

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True) # type: ignore

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
                )
        
        except Exception as e:
            print("Error processing data")



if __name__ == "__main__":
    #obj=DataIngestion()
    #strain_data,test_data=obj.initialize_data_ingestion()
    #data_trasformer=DataTransformation()
    #train_arr,test_arr,_=data_trasformer.initialize_data_transformation(train_data,test_data)
    #modeltrainer=ModelTrainer()
    #print(modeltrainer.initiate_model_trainer(train_arr,test_arr))