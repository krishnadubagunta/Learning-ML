#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created on Thu Jan 11 12:52:02 2018
    
    @author: krishna
    """
#Importing Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import Imputer, LabelEncoder, OneHotEncoder, StandardScaler as sc
from sklearn.cross_validation import train_test_split

#Importing Datasets
dataset = pd.read_csv('datasets/Data.csv')
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:,3].values

# Splitting the dataset into the Training set and Test set
X_train, X_test, Y_Train, Y_Test = train_test_split(X,Y, test_size = 0.2, random_state = 0)

# Feature Scalings
'''sc_X  = sc()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)'''
