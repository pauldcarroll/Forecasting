# Baseline section.

### 3 ways to measure baselines with Time Series Forecasting,.

import numpy as np
import pandas as pd

# 1. Take the mean for the whole dataset, and use this as the next forecast. This is a version of a baseline.

import statistics

statistics.mean(df.x)



# 2. Take a slice of the dataset and calculate this mean. This can be most useful where you have either trend and / or seasonality.
# e.g. the most recent 6 datapoints will have most relevance to a rising trend dataset of 100 long, than the first 6. 

# Where x is the length of the mean to calculate, sliding window mean function.
def most_recent_mean(df, x):
    a = len(df)
    b = a-x
    y = sum(df.iloc[b:a])
    return y/x
  
  
# 3. Run a basic linear regression model on your dataset. 

from sklearn.linear_model import LinearRegression
