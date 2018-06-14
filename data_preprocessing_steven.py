#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 09:20:50 2018

@author: vn0r4td
"""

# importing the main libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# import the data set
# iloc[rows, columns], .value removes pd dataframe to list
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

# fix missig data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = "NaN", strategy = "mean", axis = 0)
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])