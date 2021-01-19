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

#Taking the correlation for specifically 'ARRIVAL_DELAY'
delayCorr = df[df.columns[1:]].corr()['ARRIVAL_DELAY'][:].sort_values(descending=True)
print(delayCorr)

"""
Output:

ARRIVAL_DELAY          1.000000
DEPARTURE_DELAY        0.950838
AIRLINE_DELAY          0.592718
LATE_AIRCRAFT_DELAY    0.572956
AIR_SYSTEM_DELAY       0.259700
TAXI_OUT               0.245363
WEATHER_DELAY          0.235906
DEPARTURE_TIME         0.223654
WHEELS_OFF             0.217344
TAXI_IN                0.170073
SCHEDULED_DEPARTURE    0.154951
SCHEDULED_ARRIVAL      0.140565
WHEELS_ON              0.088131
ARRIVAL_TIME           0.076791
DAY                    0.070770
DAY_OF_WEEK            0.067520
FLIGHT_NUMBER          0.056163
ELAPSED_TIME           0.048448
SECURITY_DELAY         0.006070
AIR_TIME              -0.002742
SCHEDULED_TIME        -0.022043
DISTANCE              -0.023821
MONTH                       NaN
DIVERTED                    NaN
CANCELLED                   NaN
Name: ARRIVAL_DELAY, dtype: float64
"""

#As portrayed in the correlation, 'DEPARTURE_DELAY' has maximum correlation with 'ARRIVAL_DELAY'.
