#!/usr/bin/env python3

""" EDA repo to prepare and investigate your data for univariate testing """

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
import seaborn as sns
import matplotlib 
import scipy 
import sklearn

from statsmodels.tsa.api import (kpss, adfuller,seasonal_decompose, STL)
from statsmodels.tsa.seasonal import seasonal_decompose

from statsmodels.tools.eval_measures import rmspe, rmse
from sklearn.metrics import mean_absolute_percentage_error as mape
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from itertools import product
import statsmodels as sm
from pathlib import Path
import seaborn as sns
import statsmodels.api

warnings.filterwarnings('ignore')
plt.rcParams["figure.figsize"] = [12, 5]

df = pd.read_csv('../../data/weather.csv')
df['date'] = pd.to_datetime(df[['Day','Month','Year']])
df.set_index('date',inplace=True, drop=True)

rename_map = {
   
    'Total Precipitation (low resolution) daily sum [sfc]':    'Rainfall',
    'Total Cloud Cover daily mean [sfc]':'Cloudcover',
   'Sunshine Duration daily sum [sfc]': 'Sunshine',
    'Temperature daily mean [2 m above gnd]':'Temperature',
    'Temperature daily max [2 m above gnd]':'Temperature_max',
    'Relative Humidity daily mean [2 m above gnd]':'Humidity',
    'Mean Sea Level Pressure daily mean [MSL]':'Pressure_mean',
    'Shortwave Radiation daily sum [sfc]':'Radiation',
     'Wind Speed daily max [900 mb]':'max_wind_speed',
    'Wind Speed daily mean [900 mb]':'Windspeed_mean'
}

df.rename(columns=rename_map, inplace=True)

""" Univariate preparation """

def univariate_1(df):
  dfU = df.iloc[0:,5:6]
  return dfU

# Investigat the dataset, is it stationary, is there trend. 

def check_stationarity(df):
    results = adfuller(df)[1:3]
    s = 'Non-Stationary'
    if results[0] < 0.05:
        s = 'Stationary'
        print(f"'{s}\t p-value:{results[0]} \t lags:{results[1]}")
    return (s, results[0])



def univariate_prep(data, n_in=1, n_out=1, dropnan=True):
  n_vars = 1 if type(data is list else data.shape[1]
  df = pd.DataFrame(data)
  cols = list[]
                     
  for i in range(n_in, 0, -1):
      cols.append(df.shift(i))
  for i in range((0, n_out)):
      cols.append(df.shift(-i))
  msg = pd.concat(cols, axis=1)
  if dropnan:
      msg.dropna(inplace=True)
  return msg.values
                     
  
def walk_forward(data, n_test):
    predictions = list()
    train, test = train_test_split(data, n_test)
    history = [x for x in train]
                     
    return train, test, history

utrain = '../../data/utrain.pickle'                                    
train.to_pickle(utrain)
  
utest = '../../data/utest.pickle'                                       
test.to_pickle(utest)
                     
history = '../../data/history.pickle'                                       
history.to_pickle(history)                    

                
                     
 
