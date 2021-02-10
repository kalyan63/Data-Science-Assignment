import pandas as pd
import numpy as np

#Read csv file
data=pd.read_csv('CC GENERAL.csv')

#Normalize data
for i in range(1,data.shape[1]):
    min=data.iloc[:,i].min()
    max=data.iloc[:,i].max()
    if(min!=max):
        data.iloc[:,i]=(data.iloc[:,i]-min)/(max-min)
    else:
        data.iloc[:,i]=(data.iloc[:,i]-min+1)     
    # data.iloc[:,i]=data.iloc[:,i].fillna(data.iloc[:,i].mean())      
    data.iloc[:,i]=data.iloc[:,i].fillna(0)    
print("Enter Value of K (Number of clusters): ")
k=int(input())
Kcenter=list()

#Choose first centre at random
Kcenter.append(np.random.randint(data.shape[0]))
print('Centre 1 selected at random')

#Calculate other centres.
for i in range(k-1):
    print("centre {} calculated..".format(i+2))
    max_dist=0
    max_index=0
    for j in range(data.shape[0]):
        if(j in Kcenter):
            continue
        dist=0
        for cent in Kcenter:
            dist+=np.linalg.norm(data.iloc[cent,1:]-data.iloc[j,1:])
        if(dist>max_dist):
            max_dist=dist
            max_index=j
    Kcenter.append(max_index)
centre=list()
for i in Kcenter:
    centre.append(str(data.iloc[i,0]))
print(centre)        

#Find Objective Value
max_dist=0
for i in range(data.shape[0]):
    if(i in Kcenter):
        continue
    min=10**9
    for j in Kcenter:
        dist=np.linalg.norm(data.iloc[i,1:]-data.iloc[j,1:])
        if(min>dist):
            min=dist
    if(min>max_dist):
        max_dist=min       
        
print("The objective value is {} ".format(max_dist))         


