import pandas as pd

#Answer to task 1-2
df = pd.read_csv('Dataset.csv')
column1 = df['Flutter (skill out of 5)'].isna().sum()
column2 = df['Flask (skill out of 5)'].isna().sum()
column3 = df['Firebase (skill out of 5)'].isna().sum()
column4 = df['GCP (skill out of 5)'].isna().sum()
column5 = df['AWS (skill out of 5)'].isna().sum()
column6 = df['Predictive Modelling (skill out of 5)'].isna().sum()
column7 = df['EDA (skill out of 5)'].isna().sum()
column8 = df['NLP (skill out of 5)'].isna().sum()
print("The NaN values in column 1 : ", column1)
print("The NaN values in column 2 : ", column2)
print("The NaN values in column 3 : ", column3)
print("The NaN values in column 4 : ", column4)
print("The NaN values in column 5 : ", column5)
print("The NaN values in column 6 : ", column6)
print("The NaN values in column 7 : ", column7)
print("The NaN values in column 8 : ", column8)

#Answer to task 3
shape = df.shape #Taking Shape of dataframe
#Printing Number of columns 
print('Number of labels (columns) :', shape[1]-1)

#Answer to task 4
sum = 0
for i in df.iloc[74]:
  if (i != df.iloc[74][0]):
    sum += i
percent = ((df.iloc[74][-1])/sum)*100
print("Percentage :", percent)
