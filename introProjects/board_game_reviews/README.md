This analysis is conducted on a dataset containing board game names and information about their reviews, as aggregated by Board Game Geek. In addition to average ratings, features include quantity of people who have put a board game on the wish list, quantity of reviewers, maximum and minimum players needed, playing times, year published and ownership, among others. 

**Error Metric**
The error metric for the model is RMSE, or root mean squared error. This was chosen to penalize the many outliers with larger deviations from the mean and median scores. The selection of RMSE is important due to the bimodalality of this data set. Even with games containing 0 reviews moved from the data set, The vast majority of games have very few reviews, and their scores still span the entire range. 

**Clustering**
The aggregation of the datapoints for each game were clustered to yield a simple visualization and grouping of the board games. Because the games were grouped on a mean and standard deviation of all the available data, there isn't too much low level detail to be taken from this plot, but it does show that there are relatively few games with high aggregate means(>4000 on the x axis), and many, many games with relatively low aggregate means (<4000).

It's interesting to see how some boardgames stand out as exponentially more popular with both higher ratings and rating quanitites. Also, there are a very large quantity of games that have few reviews, and it would be interesting to analyze games that contain a capped number of reviews. 

**Predictive Modeling**
A quick and dirty linear regression model yielded an RMSE of 1.45. Note that the standard deviation of board game scores is 1.58. So while we're within the standard deviation, there is still room to improve. Next a Random Forest model was set up and yielded an RMSE of 1.35. More features now need to be created to better characterize the data and improve the predictive model.


TO DO:
* create more plots to better understand the existing relationships between features.
* Analyze a subset of games that fall into a smaller range of review quantities, in order to elminate the outliers that skew the data.
* Create more features.
