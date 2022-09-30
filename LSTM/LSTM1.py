### Univariate Time Series Forecasting using a LSTM neural network model 


# Import Libraries

import numpy as np
import pandas as pd
from datetime import datetime 
from datetime import timedelta
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(font_scale=1.5)
%config InlineBackend.figure_format = 'retina'
%matplotlib inline
from datetime import datetime
from datetime import timedelta
sns.set(style="ticks", rc={"lines.linewidth": 1.5})



# Read dataset in 
life = pd.read_csv('../../data/USlifeexpenctancyBirth.csv',index_col = 'TIME')
life = life.iloc[0:,5:6]
rename_map = {'Value':'Expectancy'}
life.rename(columns=rename_map, inplace=True)



#check your data
plt.figure(figsize = (20,8))
life.plot();


# Import Tensorflow libraries

import tensorflow  as tf

from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense, Dropout
from keras.layers import Bidirectional
from keras.layers import RepeatVector
from keras.layers import TimeDistributed


# Split data function 

def split_data(data, test_split):
        l = len(data)
        t_idx = round(l*(1-test_split))
        train, test = data[ : t_idx], data[t_idx : ]
        print(f'train: {len(train)} , test: {len(test)}')
        return train, test
      

# Setting your data up for a LSTM model requires two steps. 
# First you need to set your data up as two arrays.

#sequence splitter function

def split_sequence(sequence, n_steps_in, n_steps_out):
    X, y = list(), list()
    for i in range(len(sequence)):
        end_ix = i + n_steps_in
        out_end_ix = end_ix + n_steps_out
        if out_end_ix > len(sequence):
            break

        seq_x, seq_y = sequence[i:end_ix], sequence[end_ix:out_end_ix]
        X.append(seq_x)
        y.append(seq_y)
    return array(X), array(y)
  
  
# The second step is to turn the data from 2 inputs into 3. 
# LSTM models require data to be fed into the model in a 3d array.

lstm_seq = np.array(life.Expectancy)

n = 2
m = len(lstm_seq)
# define number of input steps
n_steps_in = m-n
#note that this number is also where x_input length gets defined

# number of forecast steps
n_steps_out = n

# univariate series being used here as dataset for the prediction
n_features = 1


tf.keras.backend.clear_session()
X, y = split_sequence(lstm_seq, n_steps_in, n_steps_out)
X = X.reshape((X.shape[0], X.shape[1], n_features))


# fit the LSTM model
model = Sequential()
model.add(LSTM(100, activation='relu', input_shape=(n_steps_in, n_features)))
''' extra layers for use to help refine your model 
#model.add(RepeatVector(n_steps_out))
#model.add(LSTM(100, activation='relu', return_sequences=True))
#model.add(TimeDistributed(Dense(1)))
'''
# this next line defines your forecast length. 
model.add(Dense(n_steps_out))

#fit the model, define number of epochs
model.compile(optimizer='adam', loss='mse')
model.fit(X, y, epochs=100, verbose=0)

# here used len(lstm_seq) -3, to compare the last 3 of lstm_seq against the predictions
x_input = array(lstm_seq[0:m-n])
x_input = x_input.reshape((1, n_steps_in, n_features))
yhat = model.predict(x_input, verbose=0)
print(yhat)


# Neural networks usually require a lot of data, millions of inputs in order to train a model well. 
# When using short sets of data, it may be necessary to run the model several times and average the results. 
# This is due to the stochastic nature of the model outputs. 

# Wrapping the model into a function.
# model function 
# variable setting
m = len(lstm_seq)
n = 1
n_steps_in = m-n
n_steps_out = n
n_features = 1

def lstm_data(x):

    lstm_seq = np.array(x)
    #n_steps_in, n_steps_out = m-n, n
    X, y = split_sequence(lstm_seq, n_steps_in, n_steps_out)
    X = X.reshape((X.shape[0], X.shape[1], n_features))
    #return X,y


    tf.keras.backend.clear_session()
    model = Sequential()
    model.add(LSTM(100, activation='relu', input_shape=(n_steps_in, n_features)))
    model.add(RepeatVector(n_steps_out))
    model.add(LSTM(100, activation='relu', return_sequences=True))
    model.add(TimeDistributed(Dense(1)))
    model.add(Dense(n_steps_out))
    model.compile(optimizer='adam', loss='mse')
    model.fit(X, y, epochs=1000, verbose=0)

    x_input = array(lstm_seq[0:m-n])
    x_input = x_input.reshape((1, n_steps_in, n_features))
    yhat = model.predict(x_input, verbose=0)
    #yhat = int(yhat)
    return(yhat)

  
lstm_data(life.Expectancy)
# This should produce two outputs.



# function to run the model repeatedly, and to average the results. 
def run(data, runs):
    # runs is how many times you want the model to run
    # n is equal to the last value in the dataset that will be in the model, ie n+1 is the number to predict.
    # model will use 0-n.
    # m= n-2
    # n_steps_in, n_steps_out = m-n, 1
    # n_features = 1
    # m this sets the lower boundary for the data selection into the model. Must be at least 1 less than n.
    #datax= prepare_data(data)
    results = list()
    for r in range(runs):
        result = lstm_data(data)
        #print('>#%d: %.3f' % (r+1, result))
        results.append(result)
        msg = np.mean(results)
    return(msg)

  
# Function run, 3 times here.
run(life.Expectancy,3)


