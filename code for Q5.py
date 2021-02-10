from os import read
import matplotlib.pyplot as plt
import pandas as pd

#Read Coal and Electric data of all countries
data_coal=pd.read_csv('coal_consumption_total.csv')
data_electric=pd.read_csv('electricity_generation_total.csv')

# Select few countries
country=[1,3,9,10,11,13,20,23,24,28,29,30,31,32,33,35,49,61,64,67,72,73,74,77]

#This dictionary stores all country data
Country_info=dict()

#Store coal and electricity info in respective countries
for i in country:
    Country_info[data_coal.iloc[i-1,0]]=dict()
    Country_info[data_coal.iloc[i-1,0]]["coal"]=list(data_coal.iloc[i-1,1:]/1000000) #Scale it down by 10^6
    Country_info[data_coal.iloc[i-1,0]]["elec"]=list(data_electric.iloc[i-1,1:]/1000000000) # Scale it down by 10^9
    
dates=list(data_coal)[1:]

#Save plots
for year in range(len(dates)-20):
    plt.clf()
    for i in Country_info:
        plt.scatter(Country_info[i]["coal"][year+20],Country_info[i]["elec"][year],label=i)
    plt.legend(fontsize = 'xx-small',loc='center left', bbox_to_anchor=(1, 0.5))
    plt.xlim(0,2000)
    plt.ylim(0,8000)
    plt.xlabel("Coal Consumption 10^6 tonnes")
    plt.ylabel("Electricity Production 10^9 KWH")
    plt.title(dates[year+20])
    name='p2/plot'+str(year)+'.png'
    plt.savefig(name)
