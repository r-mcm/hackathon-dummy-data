import numpy as np
import matplotlib.pyplot as plt
import random
import pandas as pd
import datetime
import json

dtStart = datetime.datetime(2022,1,1,11,34,59) #Start time given in year, month, day, hour, minute, second
health_array1 = [] #empty array to assign values to
for n in range (10000): #for loop, range number is number of rows to generate
    h = random.normalvariate(70, 7) #heartrate
    sp = random.normalvariate(105, 5) #sytolic pressure
    dp = random.normalvariate(70, 5) #diastolic pressure
    t = random.normalvariate(36.6, 0.1) #body temp
    r = random.normalvariate(14, 1) #respiration
    dt = dtStart + datetime.timedelta(0,60) #Length of time to add per row in Datetime - days, seconds, then other fields.
    dtStart = dt #adjust time for each new loop
    data = [dt, h, sp, dp, t, r] #arrange the data in an array
    health_array1.append(data) #append the data for this loop to the empty array


health_df1 = pd.DataFrame(health_array1, columns=['datetime', 'heartrate', 'systolic pressure', 'diastolic pressure', 'body temp', 'respiration']) #convert array to datafra,e    
health_df1['respiration'] = health_df1['respiration'].astype(np.int64) #cast float as integer
health_df1['heartrate'] = health_df1['heartrate'].astype(np.int64) #cast float as integer

health_df1.to_csv('healthdata.csv', sep=',', index=False) #export to csv
health_df1.to_json(r'.\healthdata.json', orient="records") #export to JSON

# un-comment to plot on a graph
# print(health_df1) #show results
# health_df1.info()

# ax = plt.gca() #plot results on a graph
# health_df1.plot(kind='line',x='datetime',y='heartrate',ax=ax)
# health_df1.plot(kind='line',x='datetime',y='sytolic pressure', color='red', ax=ax)
# health_df1.plot(kind='line',x='datetime',y='diastolic pressure',ax=ax)
# health_df1.plot(kind='line',x='datetime',y='body temp', color='red', ax=ax)
# health_df1.plot(kind='line',x='datetime',y='respiration',ax=ax)
# plt.show()

