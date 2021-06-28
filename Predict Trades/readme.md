
# BONUS TASK - PREDICT NUMBER OF TRADES AFTER 6TH MONTH

### OBJECTIVE : we want to predict the Number of Trades a customer will make after 6 months of trading 

you will find two jupyter notebook files, one predicting number trades for all customers together and the other one for a single customer ( I used cutomer with id 6276 )

## APPROACH : 


- [X] STEP 1 : Data Wrangling
- [X] STEP 2 : Data Transformation to make it stationary and supervised
- [X] STEP 3 : Building the LSTM model & evaluation
- [X] STEP 4 : Machine Learning
- [X] STEP 5 : Visualise the Prediction

## STEP 1+ 2 : DATA WRANGLING & DATA TRANSFORMATION

As We want to predict the number of Trades a customer will make after 6 months or after 3 Trades

FIRSTLY -  I grouped the date and the sum of number of Trades by groupby function

SECONDLY - Then I added a two new column

1. Data of previous months number of trades
2. Data of the difference between previous number of trades and current number of trades

LASTLY - we add the lag = 1 differencing. Specifically, to rescale the data to values between -1 and 1 to meet the default hyperbolic tangent activation function of the LSTM model.

## STEP 3 : BUILDING THE LSTM MODEL & EVALUATION

FIRSTLY - OLS regression using Formulae in the Statsmodels.formula.api

THEN -  we will fit the model and check the adjusted r squared to validate the model and we have adjusted r squared is 1 for our Regression model. Standard Errors assume that the covariance matrix of the errors is correctly specified.

FINALLY - so now we will train the model and test it to predict the number of trades the customer makes after 6 months.

## STEP 4 : MACHINE LEARNING

**STEP 1** : Scale the data using MinMax scaler

**STEP 2** : Define the Test and Train data

**STEP 3** : Fit the Model - I used the LSTM model as mentioned earlier

**STEP 4** : Make a DataFrame from the predicted value and merge this to the actual data mt: monthly trade

**STEP 5** : Plot the Number of Trades with the Predicted Number of Trades

**STEP 6** : Predict the Number of Trades for individual customer. I choose customer 6276

**STEP 7** : Visualise

![2021-06-26 (22)](https://user-images.githubusercontent.com/81169091/123558867-edd39780-d798-11eb-9a84-676482590db8.png)
![2021-06-26 (29)](https://user-images.githubusercontent.com/81169091/123558869-f62bd280-d798-11eb-8ab0-f5d68bcdb84c.png)

## CONCLUSION 

The data predicts a higher number of trades as in the case of Customer 6276 we can that he/she is predicted to more trades.

The data tells us that our model is about close to the actual number of trades in September. If we can more time series data then we can train the model better and thus a better prediction.
The data predicts a higher number of trades as in the case of Customer 6276 we can that he/she is predicted to more trades.

