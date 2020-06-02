# -*- coding: utf-8 -*-
"""
Created on Tue May 26 02:11:08 2020

@author: Geo
"""

78 // 2

78 % 2 
var = 78
mok = var // 2
div = var % 2
print("div ====>", div)
while mok != 0:
    print("mok ===>", mok)
    div = mok % 2
    print("div ====>",div)
    mok = mok // 2
    
    
    
flag = 1
next_num = var    
while flag:
    var_one_count = format(var,'b').count('1')
    next_num = next_num + 1    
    if var_one_count == format(next_num,'b').count('1'):
        flag=0
print(format(next_num,'b'))






dic = {}
first = (100- progresses[0]) / speeds[0]
dic[first] =1
for i in range(1,len(progresses)):
    print(i)
    next_value = (100- progresses[i]) / speeds[i] 
    if first > next_value:
        dic[first] +=1
    else:
        dic[next_value] =1    
        
        
processes        
        

type(list(dic.values()))





progresses = [93,20, 30, 55, 12, 12, 12]
speeds = [1,50, 30 , 5,1, 2, 3]
li = [(100- progresses[i]) / speeds[i] for i in range(len(progresses)) ]

first=li[0]
dic={}
dic[first] = 1
first_idx = 0
for i in range(len(li)):
    if len(li) == i + 1: break;
    if li[first_idx] > li[i+1]:
        dic[first] +=1
    else:
        first = li[i+1]
        dic[first] = 1
        first_idx = i + 1



        


yagu = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]    
    
import itertools



list(itertools.permutations(["1","2","3"],2))



set('123') & set('413')
    

type(set('123'))

    
    
    print((100- pro[i]) / speeds[i])
















