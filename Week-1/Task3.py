import os
import csv

from matplotlib import pyplot as plt
import numpy as np

with open("covid19.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvfile, None)

    a = ["04/03/20","05/03/20","06/03/20","07/03/20","08/03/20","09/03/20","10/03/20","11/03/20","12/03/20","13/03/20","14/03/20","15/03/20","16/03/20","17/03/20","18/03/20","19/03/20","20/03/20","21/03/20"]
    b = [] #For storing total number of cases for all dates.
    for i in range(len(a)):
        b.append(0)
    
    for row in csvreader:
        for i in range(0,len(a)):
            if (row[1] == a[i]):
                t = 0
                t += float(row[3])
                t += float(row[4])
                t += float(row[5])
                t += float(row[6])
                b[i] += t
    #print(b)

    for i in range(0, len(a)):
        print("The number of cases on", a[i], "is :", b[i])

    #For visulaizing the results..
    plt.plot(a, b)
    plt.xlabel('Date')
    plt.ylabel('Cases')
    plt.title('Date Vs. Cases')
    plt.grid(True)
    plt.savefig("Task3.png")
    plt.show()
