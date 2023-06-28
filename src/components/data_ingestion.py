import os
import datetime as dt
import numpy as np
import pandas as pd
from dataclasses import dataclass

#Local Components
#from src.components.data_transformation import DataTransformation

@dataclass
class DataIngestionConfig():
    artifact_time = "Run" + str(dt.datetime.now().strftime('%m_%d_%Y_%H_%M_%S'))
    train_data_path = os.path.join((f"artifacts+{artifact_time}"),"train.csv")
    test_data_path = os.path.join ((f"artifacts+{artifact_time}"),"test.csv")
    raw_data_path = os.path.join((f"artifacts+{artifact_time}"),"data.csv")


class DataIngestion:
    def __init__(self,raw_file):
        self.ingestion_config = DataIngestionConfig()
        self.raw_file = raw_file
        self.sub = False

    def initialize_data_ingestion(self):
            if ".csv" in str (self.raw_file):
                df = pd.read_csv(self.raw_file) 
                self.sub = True   
            elif ".xlsx" in str (self.raw_file):
                df = pd.read_excel(self.raw_file)  
                self.sub = True   
            else:
                raise Exception("File Sent is not in valid format.") 
            #os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            print("DF SUCCESS")
            print(df.head(2))
        

