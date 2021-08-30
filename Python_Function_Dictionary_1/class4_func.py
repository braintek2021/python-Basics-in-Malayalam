# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 10:18:58 2021

@author: hp
"""

###APPROACH-1###
R1=5
pi= 3.14
Area_circle_1 = pi*R1**2
print("Area of circle-1=",Area_circle_1)

R1=10
pi= 3.14
Area_circle_2 = pi*R1**2
print("Area of circle-2=",Area_circle_2)

R1=20
pi= 3.14
Area_circle_3 = pi*R1**2
print("Area of circle-3=",Area_circle_3)

###APPROACH-2###
rad= [5,10,20]
pi= 3.14
for i,r in enumerate(rad):
    Area_circle = pi*r**2
    print("circle_area_"+str(i)+"="+ str(Area_circle))
    
###APPROACH-3###
def area(radius):
    Area_circle = pi*radius**2
    
    Area_circle

rad= [5,10,20]
pi= 3.14 
for i in rad:
    Area_circle = area(i)
    print("circle_area_"+str(i)+"="+ str(Area_circle))
    

    
X= "i am global"
def call():
    X= "i am local"
    print("X_first:", X) 
call()
print("X_Second:",X)

