# Titanic Kaggle Competition
This folder contains the code and submissions created for the Kaggle Titanic Competition. 
The most recent submission recieved a score of 0.7994 / 1.0, which placed me 882 out of over 4000 submissions. This submission was generated under the guidance of the data science tutorial site [dataquest](https://www.dataquest.io). 

## Background
The goal in [Kaggle's Titanic Machine Learning Competition](http://www.kaggle.com/c/titanic) is use the provided passenger data to predict the survival of the ship's passengers as accurately as possible. This is an introductory competition intended to introduce new data scientists to nonlinear models (more on them later) and the various analysis tools available in both R and python. 

## Methodology
### Initial Submission
My initial submission was initially a logistic regression. Logistic regression analysis is a great initial method because it sets up and runs quickly and if the dataset isn't too nonlinear, it will get you most of the way there and give a solid baseline to determine the needed feature engineering and tuning more involved predictive models. 

The features utilized in this attempt were passenger class, gender, age, quanity of siblings/spouse on board, number of parents or childern on board, and port of embarkation.
### Second Submission
My second submission entailed adding a few features and using nonlinear predictive models called decision trees and and improving the tree fit through gradient tree boosting. This gradient boosting models was ensembled with the original logistic regression model to provide a more robust model capable of linear and nonlinear prediction.
**Features**
The features added include a family size quanity which is a sum of immediate family and parents/children to create a column of total family aboard. The though with this is that chance of surivival increases if a larger quantity of family is looking out for you.  A title classification feature was added to see if drawing correlations between titles and survival is useful. Lastly a feature for name length quantity was created. The 4 best features were then selected based on ANOVA F-value comparison, which included passenger class, gender, ticket price, and title.
**Predictive Model**
The training dataset was folded into 3 segments and the gradient boosting model 
was trained on those three segments successively, then tested on the others. 
This is known as cross-validation. This was run until the parameters of the 
gradient descent and logistic regression ensemble model were tuned effectively. 
