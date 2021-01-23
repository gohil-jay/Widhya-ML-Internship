#Importing necessary modules
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import roc_auc_score

#Taking the dataset into a variable
df = pd.read_csv('flights.csv', low_memory=False)
#Printing the dataset [with 5819079 rows and 31 columns]
print(df)
#Reducing the dataset to 100,000 rows.
df = df[0:100000]

#Checking the correlation of dataset entries
corr = df.corr()
#Shwoing the correlation in a tabulated manner.
print(corr)

#Creating proper dataset
df = df.values
x,y = df[:,:-1], df[:,-1]
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

#Scaling the dataset
scale = StandardScaler().fit_transform(X_train, X_test)

#Fitting the dataset
clf = DecisionTreeClassifier()
clf = clf.fit(X_train,y_train)

#Starting prediction...
prediction = clf.predict_proba(X_test)

#Calculating the AUC score
AUC = roc_auc_score(y_test, pred[:,1])
print(AUC)

"""
Output:

0.9981425213659479
"""

#Therefore, the value of AUC for task is 99.
