#this is data cleaning application
 

#importing dependencies
import pandas as pd
import numpy as np
import openpyxl
import xlrd
import os
import time
import random

#data_path = 'wallmart.xlsx'
#data_name ='jan_sales'

def data_cleaning_master(data_path,data_name):
    
    print("\nThank you for giving the details!")

    sec = random.randint(1,4)
    #print delay message
    print(f"\nplease wait for {sec} Seconds!, checking file path!")

    time.sleep(sec)
    
    #checking if the path exists
    if not os.path.exists(data_path):
        print('Incorrect Path, try again with correct path!')
        return
    else:
        #checking the file type
        if data_path.endswith('.csv'):
            print('File type is CSV')
            data = pd.read_csv(data_path, encoding_errors='ignore')

        elif data_path.endswith('.xlsx'):
            print('File type is Excel')
            data = pd.read_excel(data_path)

        else:
            print('Unknow file type')
            return
        
    #delay 
    sec = random.randint(1,4)
    print(f"please wait for {sec} Seconds!, checking total records!")
    time.sleep(sec)

    #showing number of records
    print(f"Dataset contains total rows: {data.shape[0]} \n Total Coloumns: {data.shape[1]}")

    #start cleaning

    #checking duplicate records and sending total number of duplicates
    duplicates = data.duplicated() #getting duplicate records
    total_duplicates = data.duplicated().sum()
    
     #delay 
    sec = random.randint(1,4)
    print(f"\nplease wait for {sec} Seconds!, checking total duplicates!")
    time.sleep(sec)

    print(f"\nDataset has total duplicates records: {total_duplicates}")

     #delay 
    sec = random.randint(1,4)
    print(f"\nplease wait for {sec} Seconds!, saving total duplicates rows!")
    time.sleep(sec)


    if total_duplicates > 0:
    # getting duplicate recoreds
        duplicate_records = data[duplicates]

    #saving duplicates in file
        duplicate_records.to_csv(f'{data_name}_Duplicate.csv',index=None)

    #deleting duplicates
    df = data.drop_duplicates() #in df we have cleaned data

     #delay 
    sec = random.randint(1,5)
    print(f"\nplease wait for {sec} Seconds!, checking for missing records!")
    time.sleep(sec)

    #find missing values
    total_missing_value = df.isnull().sum().sum()
    missing_values_by_colns = df.isnull().sum()



    print(f"\ndataset has total missing values {total_missing_value}")
    print(f"\ndata sets contain missing values by coloumns \n {missing_values_by_colns}")

     #delay 
    sec = random.randint(1,4)
    print(f"\nplease wait for {sec} Seconds!, cleaning the datasets")
    time.sleep(sec)

    #dealing with missing values
    columns = df.columns

    for col in columns:
        if df[col].dtype == (float,int):
            df[col] = df[col].fillna(df[col].mean()) #replacing values with mean

        else:
            df.dropna(subset=col,inplace=True) #dropping all the rows with missing records for non number col

     #delay 
    sec = random.randint(1,4)
    print(f"\nplease wait for {sec} Seconds!, exporting datasets")
    time.sleep(sec)

    #data is cleaned
    print(f"Your dataset is cleaned! , \nNumber of Rows: {df.shape[0]} \nNumber of columns: {df.shape[1]}")

    #saving clened data set
    df.to_csv(f'{data_name}_Clean_data.csv', index=None)
    print("dataset is saved!")
            

if __name__=="__main__":

    print("welcome to data cleaning app!")
 #ask the path and file name
    data_path = input("Please enter dataset path: ")

    data_name = input("Enter the dataset name: ")

 #calling function

    data_cleaning_master(data_path,data_name)

        
