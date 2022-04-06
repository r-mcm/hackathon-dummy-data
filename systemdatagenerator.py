import numpy as np
import matplotlib.pyplot as plt
import random
import pandas as pd
import datetime
import json

dtStart = datetime.datetime(2022,1,1,11,34,59) #Start time given in year, month, day, hour, minute, second
flag =  "decrease" #Flag for when battery is charging/discharging
bpstart = 100 #Start battery percentage
system_array1 = [] #empty array to assign values to
for n in range (10000): #for loop, range number is number of rows to generate
    v = random.normalvariate(90, 10) #Ventilator flow rate L/min
    wp1 = random.normalvariate(75, 5) #Waste Processing system #1 ml/min
    wp2 = random.normalvariate(60, 10) #Waste Processing system #2 ml/min
    if flag == "decrease": #if flagged as decrease, reduce battery % by 0.1 per loop
        bp = bpstart - 0.1
    if flag == "increase": #if flagged as increase, increase battery % by 1 per loop
        bp = bpstart + 1
    if bp < 10: #if battery % less than 10 set the flag to increase
        flag = "increase"
    if bp > 99: #if battery % more than 99 set the flag to decrease
        flag="decrease"
    dt = dtStart + datetime.timedelta(0,60) #Length of time to add per row in Datetime - days, seconds, then other fields.
    dtStart = dt #adjust time for each new loop
    bpstart = bp #adjust battery percentage for each loop 
    data = [dt, v, wp1, wp2, bp] #arrange the data in an array
    system_array1.append(data) #append the data for this loop to the empty array


system_df1 = pd.DataFrame(system_array1, columns=['datetime', 'ventilator flow rate', 'waste1 flow rate', 'waste2 flow rate', 'battery percentage']) #convert array to dataframe    

system_df1.to_csv('systemdata.csv', sep=',', index=False) #export to csv
system_df1.to_json(r'.\systemdata.json', orient="records") #export to JSON

# un-comment to plot on a graph
# print(system_df1) #show results
# system_df1.info()

# ax = plt.gca() #plot results on a graph
# system_df1.plot(kind='line',x='datetime',y='ventilator flow rate',ax=ax)
# system_df1.plot(kind='line',x='datetime',y='waste1 flow rate', color='red', ax=ax)
# system_df1.plot(kind='line',x='datetime',y='waste2 flow rate',ax=ax)
# system_df1.plot(kind='line',x='datetime',y='battery percentage', color='red', ax=ax)
# plt.show()

