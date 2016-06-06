# Initially Developed using pandas 0.15.2 - updated to 0.18.1 since
# need to update all the pandas rolling methods
# data source: https://www.quandl.com/data/YAHOO/INDEX_GSPC-S-P-500-Index 
# last accessed: 2015-12-07
import numpy as np
import pandas as pd
import math
from datetime import datetime as dt

def percentcalc(row):
    row['change'] = row['Close'] - row['Open']
    row['predicted_change'] = row['predicted_close'] - row['Open']
    row['predicted_percent_change'] = row['predicted_change'] / row['Open']
    row['percent_change'] = row['change'] / row['Open']
    row['percent_error'] = (row['predicted_change'] - row['change']) / row['change']
    row['direction_correct'] = math.copysign(1, row['change']) == math.copysign(1, row['predicted_change'])
    return row

mkt = pd.read_csv('sphist.csv')
mkt['Date'] = pd.to_datetime(mkt['Date'])
mkt.sort_values('Date', ascending=True,inplace=True)
#print(mkt.head(1))

#Generating Indicators
#first date: 1950-01-03
first_day = dt.strptime('1951-01-03','%Y-%m-%d')
# It's important to shift the feature rows up one, so they don't contain
# the present day's results in the predictive calculations.
# That would cause significant overfitting to occur
avg_365 = mkt['Close'].rolling(365).mean()
avg_5 = mkt['Close'].rolling(5).mean()
avg_30 = mkt['Close'].rolling(30).mean()
std_30 = mkt['Close'].rolling(30).std()

vol_avg_5 = mkt['Volume'].rolling(5).mean()
vol_std_5 = mkt['Volume'].rolling(5).std()

mkt['year'] = mkt['Date'].apply(lambda x: x.year)
mkt['mnth_day'] = mkt['Date'].apply(lambda x: x.day)
mkt['wk_day'] = mkt['Date'].apply(lambda x: x.weekday())
mkt['month'] = mkt['Date'].apply(lambda x: x.month)


mkt['avg_5'] = avg_5.shift(1)
mkt['avg_365'] = avg_365.shift(1)
mkt['avg_30'] = avg_30.shift(1)
mkt['std_30'] = std_30.shift(1)

mkt['vol_avg_5'] = vol_avg_5.shift(1)
mkt['vol_std_5'] = vol_std_5.shift(1)

mkt['wk_to_yr'] = mkt['avg_5']/mkt['avg_365']
#mkt = mkt[mkt['Date'] >= first_day]

# normally dropping rows with missing values isn't a great way to handle
# missing data, but these values are from the rolling average calculations 
# and the set now starts several months after the 'first_day' date
mkt.dropna(inplace=True)
# The Dataset now contains a rolling five and 365 day average
# along with a five day to 365 day closing price ratio


# Splitting the data into a training and test set
train = mkt[mkt['Date'] < dt.strptime('2013-01-01','%Y-%m-%d')]
test = mkt[mkt['Date'] >= dt.strptime('2013-01-01','%Y-%m-%d')]

# Error measure chosen: MAE, so it is easy to see the distance between
# the projection and the error. Error is penalized linearly here.
from sklearn.linear_model import LinearRegression
mktreg = LinearRegression()
fit_columns = ['avg_5','avg_365','wk_to_yr','avg_30','std_30']
#,'vol_avg_5','vol_std_5','year','mnth_day','wk_day','month']
mktreg.fit(train[fit_columns], train['Close'])
preds = mktreg.predict(test[fit_columns])
test['predicted_close'] = preds


#analysis
from sklearn.metrics import mean_absolute_error
mae = mean_absolute_error(test['Close'],preds)
print('mean absolute error: ',mean_absolute_error(test['Close'],preds))
# current MAE: 16.20 points
test = test.apply(percentcalc,axis=1)
dirpercent = test['direction_correct'].sum() / test.shape[0]
print('direction guessed correctly:',dirpercent)
# currently, the direction is guessed correctly 51% of the time - 
# lots of work needs to be done to make this more interesting
 
