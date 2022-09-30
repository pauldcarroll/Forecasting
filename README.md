# Forecasting
A repo of different forecasting methods for different situations.


Within this repo, there are several ways of going about Time Series Forecasting (TSF). 
When you come to look at a dataset, and the question is, how do I predict y from my existing data, quite often the area that's hardest is knowing where to begin, how to go about the forecasting, and what method is most appropriate, and will give you the best results.

What this repo will do, is try and guide you through this forest, so you can see the wood for the trees. The repo will only cover numerical forecasting, so regression style forecasting, as opposed to classification (binary) forecasting. 

When it comes to Time Series Forecasting, or any other type of modeling, knowing whether your model is performing well is critical. Whether your dataset for prediction is univariate (one variable in, one out), or multivariate (multiple variables in, can be multiple variables out), and how far you want to forecast, the first step is to establish a baseline, from which you can compare and contrast the various models. 
In this repo we will use two measures to compare and contrast each model against the baseline, Residual Mean Squared Error (RMSE) and Mean Absolute Error, (MAE). In TSF, these work together. A very good starting place to establish a baseline is to look at the mean. For your dataset, this can be the last 3 months to predict the next month, or the last 6 periods to predict period 7. From my experience, it can be tough to beat these styles of mean forecasts. 
Additionally we will use a basic linear regression model for these scores, and use this as a model baseline. 


### Know your data

The starting point for any data analysis, is to know your data. What do I mean by this?
Lets go through a 5 step process specifically for Time Series Forecasting. 

1. Is your dataset univariate of multivariate. I.e. do you just a list of Temperatures for the last x years, and are trying to forecast the next week's temperatures. Or do you have a dataframe of variables about weather, so sunshine hours, cloudcover, rainfall, and are trying to forecast the temperature from these other variables. This way of thinking can be applied to any dataset. Previous stock prices for next few days' stock price, or patient's admission dataset and history to forecast their outcome at time of admission, or length of stay post admission.
The answer to this will help you decide which models to use in this repo. 

2. Critical within model accuracy is data preparation. Is your data stationary? What does this mean. Stock prices are a good example of this, as is energy usage over a year. Both of these over time, will display either trend or seasonality or both. In order for your models to perform better, a time series will need to be made stationary. If youre time series is not stationary, it came be made stationary by differencing. What this means, is instead of training a model on a series of stock prices, the model performs a lot better on the differences in the period stock prices, so +0.5, -0.25, +0.75, as opposed to 175, 175.5, 175.25, 176. In stats we call this the p value. 

5. Examine your model and your data. What are you trying to forecast? Is it bank holiday attendances in hospital A&E. If so, if your model performing badly and you don't know why? Take a step back here and look at the data you're feeding into your model. For example if you have A&E attendance figures for the last 5 years, and you're trying to forecast the next three bank holiday attendances, why are you feeding in all the datapoints? Split your data into bank holiday data and other data, or weekend data, bank holiday data and non-weekend data, and re-run your models. Forecasting isn't an exact science, but being prepared to iterate over the numbers, refine your models by experimentation not just on hyper-parameters but also on datasets used for training. You may see your results improve dramatically following this. 



## Baselines

Lets begin this by finding the mean of the dataset. 

With Time Series data you can average the whole length of the dataset, and take this as your next forecast baseline.
This works if your data doesn't have trend, or the mean takes into account a whole seasonal period. 

Code for this is in the baseline code section. 
