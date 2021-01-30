#Impoting necessary packages and libraries
import quandl, math
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing, svm
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

#Defining the API key for Qyandl
auth_tok = "zT6DNLxAdJuUdyySgxGN"

#Taking the data from Quandle into variable 'data'
data = quandl.get("EOD/AAPL", trim_start = "2000-12-12", trim_end = "2020-12-30", authtoken=auth_tok)

#Taking only necessary columns in dataset (for creating new columns)
data = data[['Adj_Open',  'Adj_High',  'Adj_Low',  'Adj_Close', 'Adj_Volume']]

#Creating new columns, and adding data for them using specific formula
data['HL_PCT'] = (data['Adj_High'] - data['Adj_Low']) / data['Adj_Close'] * 100.0
data['PCT_change'] = (data['Adj_Close'] - data['Adj_Open']) / data['Adj_Open'] * 100.0

#Taking only ncessary columns in final working dataset
data = data[['Adj_Close', 'HL_PCT', 'PCT_change', 'Adj_Volume']]

#Defining forecasting column
forecast_col = 'Adj_Close'

#Replacing NaN values with '-99999' value which is considered as an outlier by most ML classifiers
data.fillna(value=-99999, inplace=True)

#Forecasting out 1% of the dataset's length
forecast_out = int(math.ceil(0.01 * len(data)))

#Adding a new coumn for 'label'
data['label'] = data[forecast_col].shift(-forecast_out)

#Preparing X and y
X = np.array(data.drop(['label'], 1))
X = preprocessing.scale(X)
X = X[:-forecast_out]
data.dropna(inplace=True) #Dropping NaN values
y = np.array(data['label'])

#Splitting the data into 80:20 ratio
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

#Training the linear regression model
clf = LinearRegression(n_jobs=-1)
clf.fit(X_train, y_train)

#Predicting y values
y_predicted = clf.predict(X_test)
#print(y_predicted)

#Finding MSE value
MSE = mean_squared_error(y_test, y_predicted)
print("Mean Squared Error: %.15f" %MSE)

# Finding confidence value
confidence = clf.score(X_test, y_test)
print("Confidence:         %.15f" %confidence)

"""
Output -->

Mean Squared Error: 1.600826094253702
Confidence:         0.965791363940355
"""
