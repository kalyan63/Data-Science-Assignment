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
    data.iloc[:,i]=data.iloc[:,i].fillna(0)         
print("Enter Value of K")
k=int(input())
Kcenter=list(range(1,k+1))

#This is used to find the cost of K center
def cost(center):
    max_dist=0
    for i in range(data.shape[0]):
        if(i in center):
            continue
        min=10**9
        for j in center:
            dist=np.linalg.norm(data.iloc[i,1:]-data.iloc[j,1:])
            if(min>dist):
                min=dist
        if(min>max_dist):
            max_dist=min 
    return max_dist     

#Concider 1st centre and iterate through all points to find opt centre
opt_center=Kcenter[:]
opt_cost=cost(Kcenter)

#Iterate through all points which takes ((10^4)^2)^4 for just 2 centers. Need super computer to calculate this.
loop=0
for i in range(data.shape[0]):
    loop+=1
    if(loop%500==0):
        print("Done 500")
    for j in range(i+1,data.shape[0]):
        Kcenter=list([i,j])
        costi=cost(Kcenter)
        if(costi<opt_cost):
            opt_cost=costi
            opt_center=Kcenter

# Print optimal centre           
centre=list()
for i in opt_center:
    centre.append(str(data.iloc[i,0]))
print(centre)        
print("OPtimal cost is {} ".format(opt_cost))