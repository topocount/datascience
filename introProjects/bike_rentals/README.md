
This bike rentals dataset has served as an interesting way to explore the effectiveness of predictive modelling algorithms, along with feature engineering and selection. It contains bike rental data by the hour and date, along with pertinent weather and season data. The rental data is broken down between casual (unregistered) and registered users. Developing and analyzing a predictive model around registered users on weekdays might allow us to better understand commuting patterns and bicycling adoption over time. Analyzing use by casual users might allow us to understand tourist usage based on seasonality and weather. While analyzing total bike usage and demand is useful, there is definitely further insight to be gained by conducting separate analysis on registered and casual users.

**Error Metric Selection**
Root Mean squared error is used to better capture the existence of outliers in the data. 

**Random Forests**
A Random Forest was found to yield a RMSE of about 80 bikes. adding a weather index feature that aggregated temperature, humidity and wind speed into one metric brought the error down to about 77 bikes. Future improvement might include using a gradient boosting model to better improve the predictive model.
To Do:
* Attempt to predict casual and registered users and see what their output is.
* Try out a gradient boosting predictive model
* create aggregate weather index with temperature, humidity and wind parameters - **DONE**
