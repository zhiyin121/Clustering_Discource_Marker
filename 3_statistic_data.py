import numpy as np
import matplotlib.pyplot as plt


f = open('space_dan_normalize.txt', 'r', encoding = 'utf-8')

percentage = []
for line in f.readlines():
    lst = line.rstrip('\n').split('\t ')[1:]
    #print(lst)
    count = 0
    for i in range(len(lst)):
        count += float(lst[i])
    percentage.append(count/1000)
print(percentage)        

a = 0 #<=0.0025
b = 0 #0.0025<x<=0.005
c = 0 #0.005<x<=0.0075
d = 0 #0.0075<x<=0.01
e = 0 #0.01<x<=0.0125
f = 0 #0.0125<x<=0.015
g = 0 #0.015<x<=0.0175
h = 0 #>0.0175

for i in range(len(percentage)):
    if percentage[i] <= 0.0025:
        a += 1
    if 0.0025 < percentage[i] <= 0.005:
        b += 1
    if 0.005 < percentage[i] <= 0.0075:
        c += 1
    if 0.0075 < percentage[i] <= 0.01:
        d += 1
    if 0.01 < percentage[i] <= 0.0125:
        e += 1
    if 0.0125 < percentage[i] <= 0.015:
        f += 1
    if 0.015 < percentage[i] <= 0.0175:
        g += 1
    if percentage[i] > 0.0175:
        h += 1

print(a,b,c,d,e,f,g,h)
