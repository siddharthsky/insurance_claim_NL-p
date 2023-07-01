import os
import numpy as np
import pandas as pd



class DataTransformation:
    def __init__(self,df):
         self.df=df
         self.initialize_data_transformation()


    def initialize_data_transformation(self):
            print("Transfromed data")
            return self.df
