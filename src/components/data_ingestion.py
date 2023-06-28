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
    train_data_path = os.path.join((f"artifacts"+{artifact_time}),"train.csv")
    test_data_path = os.path.join ((f"artifacts"+{artifact_time}),"test.csv")
    raw_data_path = os.path.join((f"artifacts"+{artifact_time}),"data.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initialize_data_ingestion(self):
        try:
            for i in os.listdir("temp"):
                raw_file = i
            
            
