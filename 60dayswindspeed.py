import numpy as np
import pickle
import pandas as pd
import os

u =[]
v=[]
w = []
windspeed = []

for filename in os.listdir('D:/windata/windspeed_pk/u'):
    with open('D:/windata/windspeed_pk/u/' + filename , 'rb') as file_u:
        data_u = pickle.load(file_u)
    for each in data_u[0:6]:
        #print(each)
        #print('-'*20)
        print(each[0])
        #print('-'*20)
        temp_u = each[1][470][665]
        u.append(temp_u)
        temp_u = []
    #print(u)


for filename in os.listdir('D:/windata/windspeed_pk/v'):
    with open('D:/windata/windspeed_pk/v/' + filename , 'rb') as file_v:
        data_v = pickle.load(file_v)
    for each in data_v[0:6]:
        #print(each)
        #print('-'*20)
        print(each[0])
        #print('-'*20)
        temp_v = each[1][470][665]
        v.append(temp_v)
        temp_v = []
    #print(v)


for filename in os.listdir('D:/windata/windspeed_pk/w'):
    with open('D:/windata/windspeed_pk/w/' + filename , 'rb') as file_w:
        data_w = pickle.load(file_w)
    for each in data_w[0:6]:
        #print(each)
        #print('-'*20)
        print(each[0])
        #print('-'*20)
        temp_w = each[1][470][665]
        w.append(temp_w)
        temp_w = []
    print(w)




#name = ['u','v','w']
name = ['u','v']
x1 = list(range(20210601,20210631))
x2 = list(range(20210701,20210732))
name2 = x1 + x2
wind = []
wind.append(u,)
wind.append(v)
#wind.append(w)

test = pd.DataFrame(columns=name,data=wind)
test.to_csv('D:/windata/123.csv',encoding = 'gbk')


rows = zip(u,v)
import csv

with open('D:/windata/test.csv', "w") as f:
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)