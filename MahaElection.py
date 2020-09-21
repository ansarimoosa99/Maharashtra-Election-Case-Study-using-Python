import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import collections
# Merging two excel files
df=pd.DataFrame()

for f in ['maharashtraresults2009.xlsx','maharashtraresults2014.xlsx']:
    data=pd.read_excel(f,'Sheet1')
    df=df.append(data)
df.to_excel('CombinedData.xlsx')
data=pd.read_excel('CombinedData.xlsx')
print(data)

plt.figure(figsize=(8,4))
plt.scatter(data['PARTYNAME'],data['SEATS'],c='blue')
plt.xlabel("Party")
plt.ylabel("Seats Won")
plt.xticks(rotation=90)
plt.show()

#Adding the no. of seats of parties

final_Data={}
for i in data['PARTYNAME']:
    x=i
    t1=(data[(data.PARTYNAME==i) & (data.YEAR==2009)].SEATS).tolist()#retriving seats of similar partyname and at the same time conveting it to a list from panda.Series datatype
    t2=(data[(data.PARTYNAME==i) & (data.YEAR==2014)].SEATS).tolist()
    t3=t2+t1
    print("------------------")
    print("Name of the party=",i)
    print("Number of seats",int(sum(t3)))
    final_Data.update({i : int(sum(t3))})
  
#Plotting the data of Dictionary 
    
plt.bar(final_Data.keys(),final_Data.values(),color='green')
plt.xlabel("Party")
plt.ylabel("Seats Won")
plt.xticks(rotation=90)
plt.show()

#Perfomance

print("\nThe change in perfomance is as follows")
for i in data['PARTYNAME']:
    x=i
    t2=(data[(data.PARTYNAME==i) & (data.YEAR==2014)].SEATS).tolist()#retriving seats of similar partyname and at the same time conveting it to a list from panda.Series datatype
    t1=(data[(data.PARTYNAME==i) & (data.YEAR==2009)].SEATS).tolist()
    diff=sum(t1[0:])-sum(t2[0:])
    if diff>0:
        print("Party name:",x)
        print("Loss from 2009 to 2014=",int(diff))
    else:
        if diff<0:
            print("Party Name",x)
            print("Gain from 2009 to 2014=",abs(int(diff)))
        else:
             print("Party Name",x)
             print("No change from 2009 to 2014=",int(diff))