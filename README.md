# Forecasting
A repo of different forecasting methods appropriate for different situations.


Within this repo, there are several ways of going about Time Series Forecasting (TSF). 
When you come to look at a dataset, and the question is, how do I predict from my existing, quite often the area that's hardest is knowing where to begin, how to go about the forecasting, and what method is most appropriate, and will give you the best results.

What this repo will do, is try and guide you through this forest, so you can see the wood for the trees. The repo will only cover numerical forecasting, so regression style forecasting, as opposed to classification (binary) forecasting. 

When it comes to Time Series Forecasting, or any other type of modeling, knowing whether your model is performing well is critical. Whether your dataset for prediction is univariate (one variable in, one out), or multivariate (multiple variables in, can be multiple variables out), and how far you want to forecast, the first step is to establish a baseline, from which you can compare and contrast the various models. 
In this repo we will use two measures to compare and contrast each model against the baseline, Residual Mean Squared Error (RMSE) and Mean Absolute Error, (MAE). In TSF, these work together. A very good starting place to establish a baseline is to look at the mean. For your dataset, this can be the last 3 months to predict the next month, or the last 6 periods to predict period 7. From my experience, it can be tough to beat these styles of mean forecasts. 
Additionally we will use a basic linear regression model for these scores, and use this as a model baseline. 




