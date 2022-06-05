# -*- coding: utf-8 -*-
"""
Created on Tue May 31 12:27:15 2022

@author: sudhakar
"""

#Use decision trees to prepare a model on fraud data treating those who have taxable_income <= 30000 as "Risky" and others are "Good"

#Data Description :

#Undergrad : person is under graduated or not

#Marital.Status : marital status of a person

#Taxable.Income : Taxable income is the amount of how much tax an individual owes to the government

#Work Experience : Work experience of an individual person

#Urban : Whether that person belongs to urban area or not

import pandas as pd
import pandas as pd
from sklearn.model_selection import  train_test_split
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn import preprocessing
import matplotlib.pyplot as plt

fraud_df =pd.read_csv(r'/Downloads')
fraud_df
fraud_df.info()

fraud_data=fraud_df

#Label encoding for categorical data
label_encoder=preprocessing.labelEncoder
fraud_data['Undergrad']=lable_eencoder.fit_transform(fraud_data['Undergrad'])


