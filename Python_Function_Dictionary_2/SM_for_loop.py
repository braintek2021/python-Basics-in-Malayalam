# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
### SUPERMARKET###
print("Welcome to the 'Etha picdicho' Supermarket!")
print("Please provide your vegetable list to your vendor")
veg_list=['tomato','onion','carrot','brinjal']
price_list=[20,30,60,35]
print("Kindly type 'Know my price' to know the price of your items")
price_total=[]
def price_calc(user_input):
    if user_choice == 'Know my price':
        for j in range(len(veg_list)): 
            item = float(input("How many "+veg_list[j]+"( in kg?): "))
            price=price_list[j]*item 
            print('your price =',price)
            price_total.append(price)
        print(price_total)
        total_price=sum(price_total)
        print("The total cost is Rs",total_price)
        pay = float(input("Please enter an amount to pay for the fruits and vegetables: "))
        while pay < total_price:
            pay = float(input("Please enter an amount more than payment: "))
        change = pay - total_price
        print("Your change will be Rs", change)
        print('Thank you, next please')

    else:
        print('I dont know your entry, please retry')                
while True:
    user_choice = input("Please enter your inputs: ")
    price_calc(user_choice)
    #break
   
    
        

    

    


