# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 05:23:28 2021

@author: hp
"""

import sys
#print(sys.version)
###VARIABLES###

a=5
#print(a)
b=10
c= a+b#EXPRESSIONS
#print(c)
e=a*b
#print(e)
f=2.5
###TYPE###
#print(type(a))
#print(type(f))
name="Hello World"
#print(type(name))
###DIR###
#print(dir(a))
#print(dir(name))
name = name.lower()
#print(name)

splt= name.split(' ')
#print(splt)
#print(type(splt))
#print(dir(splt))
w= "welcome"
splt.append(w)
#print(splt.index('world'))

tup=tuple(splt) 
#print(tup)
print(type(tup))
print(dir(tup))