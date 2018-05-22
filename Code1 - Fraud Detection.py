# -*- coding: utf-8 -*-
"""
Created on Tue May 22 18:22:07 2018

Purpose:
    Basic Data Analysis on the Fraude detection Kaggle Problem

https://www.kaggle.com/ntnu-testimon/banksim1

@author: Prakash.Tiwari
"""
import numpy as np
import pandas as pd
import os
os.chdir(u'C:\Work\Daily Tasks\Machine Learning Udemy\Kaggle\Fraud Detection')

os.listdir(u'C:\Work\Daily Tasks\Machine Learning Udemy\Kaggle\Fraud Detection')

""""
Basic Data Analysis:
    
    . Missing value in columns - Done
    . Percentage missing value in columns - Done
    . #Unique in each columns - Done
    . Some sample values of each column - Done

Result: zipCodeOri and zipMerchant are not helpful as they have only one value. 

Check correlation of different variables with fraud
Bucket amounts into different bins and see correlation with fraud
    
"""

bank_data = pd.read_csv('bs140513_032310.csv')

#Counts
no_obs = len(bank_data)
no_features = len(bank_data.columns)
no_fraud = len(bank_data[bank_data['fraud'] ==1])
no_fair = no_obs - no_fraud


#Treat ' ' and np.inf as NA
pd.options.mode.use_inf_as_na = False


#Missing values, Unique, Sample values
#Check if there is missing value in a column and what is the percentage_missing. 

has_missing = []
Percentage_missing = []
Unique_values = []
Sample_values = []

for column in bank_data.columns:
    print('Running for Column {}'.format(column))
    
    Unique_values.append(len(bank_data[column].unique()))
    Sample_values.append(np.array(bank_data[column].unique()[:3]))
    
    if column in bank_data.dropna(axis=1, how ='any').columns:
        has_missing.append('No')
        Percentage_missing.append(0)
    else:
        has_missing.append('Yes')
        Percentage_missing.append(len(bank_data.column[bank_data.column.isnull()])/float(no_obs))

#Alternate way of getting columns with missing values
bank_data.dropna(axis=1, how ='any').columns
        
overview_data = pd.DataFrame(data = np.transpose([has_missing, Percentage_missing, Unique_values, Sample_values]) ,
                             index = bank_data.columns,
                             columns = ['Missing', 'Total Missing', 'Unique_values', 'Sample_values'])
        