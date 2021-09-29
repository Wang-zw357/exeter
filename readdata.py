'''
import os
from re import X
os.getcwd()
os.chdir('E://winddata')
'''
import numpy as np
import pickle

u =[]
v=[]
w = []
windspeed = []

with open('D:/windata/windspeed_pk/2021060100_WSEuro4_wind_u_sl_1000hPa_001054.pk', 'rb') as file_u:
    data_u = pickle.load(file_u)
print('u')

for each in data_u:
    #print(each)
    #print('-'*20)
    #print(each[0])
    #print('-'*20)
    #print(each[1][470][665])
    temp_u = each[1][470][665]
    u.append(temp_u)
print(u)

with open('D:/windata/windspeed_pk/2021060100_WSEuro4_wind_v_sl_1000hPa_001054.pk', 'rb') as file_v:
    data_v = pickle.load(file_v)
print('v')

for each in data_v:
    #print(each)
    #print('-'*20)
    #print(each[0])
    #print('-'*20)
    #print(each[1][470][665])
    temp_v = each[1][470][665]
    v.append(temp_v)
print(v)

v2 = [i/2 for i in v]
print(v2)

ws = list(np.add(u,v2))
ws2 = [round(i,2) for i in ws]
print(ws2)


with open('D:/windata/windspeed_pk/2021060100_WSEuro4_wind_w_sl_1000hPa_001054.pk', 'rb') as file_w:
    data_w = pickle.load(file_w)
print('w')

for each in data_w:
    #print(each)
    #print('-'*20)
    #print(each[0])
    #print('-'*20)
    temp_w = each[1][470][665]
    w.append(temp_w)
print(w)


for filename in os.listdir('D:/windata/windspeed_pk'):
    with open('D:/windata/windspeed_pk/' + filename , 'rb') as file_w:
        data_w = pickle.load(file_w)
    for each in data_w[0:6]:
        #print(each)
        #print('-'*20)
        #print(each[0])
        #print('-'*20)
        temp_w = each[1][470][665]
        w.append(temp_w)
    print(w)


