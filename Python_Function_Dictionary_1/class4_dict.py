# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 06:01:35 2021

@author: hp
"""
total = 0
prices = {
    "Tomato": 20,
    "Onion": 30,
    "Carrot": 60,
    "Bringal": 35
}

print(type(prices))
print(prices["Tomato"])



Qty = {
    "Tomato": 2,
    "Onion": 1,
    "Carrot": 1,
    "Bringal": 1
}

for key in prices:
    print(key,":",prices[key])
    print("price: %s" % prices[key])
    print("stock: %s" % Qty[key])
    
for key in prices:
    Veg_price = prices[key] * Qty[key]
    print(Veg_price) 
    total = total + Veg_price

print("The total cost is Rs",total)