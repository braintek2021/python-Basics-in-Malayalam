# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
Main_list=['tomato','onion','carrot','brinjal','pen',' book', 'scissor']
Veg_list=Main_list[:4]
sta_list=Main_list[4:]
#sta_list2=Main_list[-3:]
print(Veg_list)
print(sta_list)
#print(sta_list2)
print(range(len(Veg_list)))
for i in range(len(Veg_list)):
    print(i+1,Veg_list[i])
# Vendor List
for ind,item in enumerate(Veg_list):
    print(ind+1,item)
    
Vendor_list=['potato','celery','peas','tomato','onion','carrot','beetroot','cabbage']
for k in range(len(Veg_list)):
    for j in range(len(Vendor_list)):
        if Veg_list[k]==Vendor_list[j]:
            print(Veg_list[k],'is available')
        else:
            print(Veg_list[k],'is not available')
            

Ava_list=[]
Not_Ava_list=[]
for veg in Veg_list:
   if veg in Vendor_list:
       Ava_list.append(veg)
   else:
        Not_Ava_list.append(veg)
     
print(Ava_list)
print(Not_Ava_list)
###list comprehension###
Main_list=['tomato','onion','carrot','brinjal','pen',' book', 'scissor']
Vendor_list=['potato','celery','peas','tomato','onion','carrot','beetroot','cabbage']
Ava_list2= [veg for veg in Veg_list if veg in Vendor_list]
print('Ava_list2=',Ava_list2)
Not_Ava_list2=[veg for veg in Veg_list if veg not in Vendor_list]
print('Not_Ava_list2=',Not_Ava_list2)


### Use of set###
set1 = set(Veg_list)
set2 = set(Vendor_list)
matched = set1.intersection(set2)
unmatched = set1.symmetric_difference(set2) 
# print(type(matched))
# print(unmatched)
print(dir(set1))



import time
from datetime import datetime

now = datetime.now()
print(now)

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
