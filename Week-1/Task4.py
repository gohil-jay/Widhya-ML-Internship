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
    c = [] #For storing all R(s)
    
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

    #Calculating r for all dates and storing them in c[]
    for i in range(0,len(b)-1):
        x = float((b[i+1]-b[i])/b[i])
        c.append(x)    
    #print(c)

    #Calculating the average 'r'
    k = 0.00
    for i in c:
        k += i
    r = k/len(c)
    #print(r)

    #Calculating Pt
    Po = 31
    time = 26
    Pt = (Po*(2.71828*(r*time)))
    print("The value of Pt :", Pt)

    d = c
    d.append(0) #For rectifying r value on 21st March (as data on 22nd March is not available)

    #For visulaizing the results..
    plt.plot(a, d)
    plt.xlabel('date')
    plt.ylabel('r Value')
    plt.title('Date Vs. r-value plot')
    plt.grid(True)
    plt.savefig("Task4.png")
    plt.show()
