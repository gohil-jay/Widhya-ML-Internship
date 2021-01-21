#Importing necessary modules
import pandas as pd

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

#Creating new row for recording arrival delay graeter than 15 minutes (with values 0 & 1)
delayFifteen = []

#Inputting the row with data
for row in df['ARRIVAL_DELAY']:
    if row > 15:
        delayFifteen.append(1)
    else:
        delayFifteen.append(0)

#Adding the row in df
df['delayFifteen'] = delayFifteen

#Printing the values
values = df['delayFifteen'].value_counts()
print(values)

"""
Output:

0    63779
1    36221
Name: result, dtype: int64

"""

#Thus, there are 36221 flight delays that were greater than 15 minutes.
