"""Creating a new column 'time' with time passed in numerical value."""

#Importing necessary modules
import csv

#Creating array to store numerical (time spent) values
arr = ['time']

#Traversing through CSV file and adding 'time spent' numerical values into 'arr' array
with open("instagram_reach.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvfile, None)
    
    for row in csvreader:
        x = row[6]
        y = int(x[0:2])
        arr.append(y)

# Open the input_file in read mode and output_file in write mode, and creating new file (replica of instagram_reach) with addition of 'time' column with numerical values for'time spent' for instagram post.
with open('instagram_reach.csv', 'r') as read_obj, \
        open('clean_data.csv', 'w', newline='') as write_obj:

    # Create a csv.reader object from the input file object
    csv_reader = reader(read_obj)
    # Create a csv.writer object from the output file object
    csv_writer = writer(write_obj)

    #Adding the values into new column
    i = 0
    for row in csv_reader:
        row.append(arr[i])
        csv_writer.writerow(row)
        i += 1

""" New row added into new replica file 'clean_data.csv'. """

"""----------------------------------------------------------------"""
"""----------------------------------------------------------------"""

#Prediction Type1 (MultiVariate Regression).
#Prediction for Likes, with input of 'Followers' and 'time'.

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

#Reading CSV file
df = pd.read_csv('clean_data.csv')

#Dropping irrelevant columns
df = df.drop(df.columns[[0]], axis=1)
df = df.drop(['S.No','USERNAME', 'Caption', 'Hashtags', 'Time since posted'], axis=1)
#print(df) [All colums are dropped now]

#Drppoing 'Likes' column from 'X' and adding it into 'y'
X = df.drop('Likes', axis=1)
y = df[['Likes']]
#print(X)
#print(y)

#Splliting the dataset into 80:20 ratio
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=1)

#Training the model
reg = LinearRegression()
reg.fit(X_train[['Followers','time']], y_train)

#Making prediction on test dataset
y_predicted = reg.predict(X_test[['Followers','time']])

#Printing the prediction's MSE value
print("Mean squared error: %.2f" % mean_squared_error(y_test, y_predicted))
#Gives value of '953.76'

#Making prediction on custom value
pred = reg.predict([[300,10]])
print("The prediction for values '300' and '10' -->", pred[0][0])
#Gives value of '108.63581186362067'

"""-----------------------------------------------------------------"""
"""-----------------------------------------------------------------"""
                 
#Prediction Type2 (MultiVariate Regression).
#Prediction for time, with input of 'Followers' and 'Likes'

"""
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
"""

#Reading CSV file
df = pd.read_csv('clean_data.csv')

#Dropping irrelevant columns
df = df.drop(df.columns[[0]], axis=1)
df = df.drop(['S.No','USERNAME', 'Caption', 'Hashtags', 'Time since posted'], axis=1)
#print(df) [All colums are dropped now]

#Drppoing 'time' column from 'X' and adding it into 'y'
X = df.drop('time', axis=1)
y = df[['time']]
#print(X)
#print(y)

#Splliting the dataset into 80:20 ratio
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

#Training the model
reg = LinearRegression()
reg.fit(X_train[['Followers','Likes']], y_train)

#Making prediction on test dataset
y_predicted = reg.predict(X_test[['Followers','Likes']])

#Printing the prediction's MSE value
print("Mean squared error: %.2f" % mean_squared_error(y_test, y_predicted))
#Gives value of '5.25'

#Making prediction on custom value
pred = reg.predict([[300,10]])
print("The prediction for values '300' and '10' -->", pred[0][0])
#Gives value of '1.9003413803950806'
