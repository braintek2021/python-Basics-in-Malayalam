# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 05:03:14 2021

@author: hp
"""


### SUPERMARKET ###

import time
from datetime import datetime
now = datetime.now()
print(now)
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
time.sleep(2)

print("Welcome to 'Etha pidicho' Supermarket!")
print("1. Tomato (20 per Kg)")
print("2. Onion (30 per Kg)")
print("3. Carrot (60 per Kg)")
print("4. Bringal (35 per Kg)")
print("5. Checkout")
price=0
try:
    while True:
        user_choice = int(input("please enter your number: "))
        if user_choice == 1:
          Tomatos = int(input("How many tomatoes(in kg?): "))
          price_tomato=Tomatos*20
          print('Tomato price',price_tomato)
        if user_choice == 2:
          Onion= int(input("How many onions(in kg?): "))
          price_onion=Onion*30
          print('Onion price',price_onion)
        if user_choice == 3:
          carrot= int(input("How many carrots(in kg?): "))
          price_carrot=carrot*60
          print('Carrot price',price_carrot)
        if user_choice == 4:
          brinjal= int(input("How many brinjals(in kg?): "))
          price_brinjal=brinjal*35 
          print('Brinjal price',price_brinjal)
        if user_choice == 5:
            total_price = price +  price_tomato+price_onion+price_carrot+price_brinjal
            print("The total cost is Rs",total_price)
            pay = float(input("Please enter an amount to pay for the fruits and vegetables: "))
            while pay < total_price:
                pay = float(input("Please enter an amount more than payment: "))
            change = pay - total_price
            print("Your change will be Rs", change)

except KeyboardInterrupt:
    print("Pressed Ctrl-C to Exit")
    pass    