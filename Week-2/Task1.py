#Importing necessary modules
import pandas as pd

#Taking the dataset into a variable
df = pd.read_csv('flights.csv', low_memory=False)
#Printing the dataset [with 5819079 rows and 31 columns]
print(df)
#Reducing the dataset to 100,000 rows.
df = df[0:100000]

#Taking the count of 'DIVERTED' occurence
diversion = df.value_counts('DIVERTED')
print(diversion)

"""
Output:

DIVERTED
0    99776
1      224
dtype: int64

"""

#Thus, the number of diverted flightes is 224.
