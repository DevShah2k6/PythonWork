import pandas as pd



def dataset_analysis(crop):
    print("----------------CHECKING NULL VALUES----------")
    print(crop.isnull().sum())
    print("----------------CHECKING DUPLICATED VALUES---------")
    print(crop.duplicated().sum())
    print("----------------DATASET INFORMATION----------------")
    print(crop.info())
    print("-----------STATISCAL SUMMARY OF DATASET--------------")
    print(crop.describe())
    print("----------SHOWING FIRST FIVE ROWS--------------------")
    print(crop.head())
    print("-----------SHOWING LAST FIVE ROWS--------------------")
    print(crop.tail())