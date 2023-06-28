import os
import datetime as dt
import numpy as np
import pandas as pd
from dataclasses import dataclass

#Local Components
from src.components.data_viz import VizStore
#from src.components.data_transformation import DataTransformation

@dataclass
class DataIngestionConfig():
    artifact_time = "Run " + str(dt.datetime.now().strftime('%m_%d_%Y_%H_%M'))
    train_data_path = os.path.join((f"artifacts\{artifact_time}"),"train.csv")
    test_data_path = os.path.join ((f"artifacts\{artifact_time}"),"test.csv")
    raw_data_path = os.path.join((f"artifacts\{artifact_time}"),"data.csv")
    print(raw_data_path)

class DataIngestion:
    def __init__(self,raw_file):
        self.ingestion_config = DataIngestionConfig()
        self.raw_file = raw_file
        self.sub = False

    def initialize_data_ingestion(self):
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            if ".csv" in str (self.raw_file):
                df = pd.read_csv(self.raw_file)
                df.to_csv(self.ingestion_config.raw_data_path)
                self.sub = True   
            elif ".xlsx" in str (self.raw_file):
                df = pd.read_excel(self.raw_file) 
                df.to_csv(self.ingestion_config.raw_data_path) 
                self.sub = True   
            else:
                raise Exception("File Sent is not in valid format.") 
            

            #Add code to split data set here

            print("DF SUCCESS")
            print(df.head(2))
            GUIviz = VizStore(df)

