# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
### SUPERMARKET###
print("Welcome to the 'Etha pidicho' Supermarket!")
# print("Please provide your vegetable list to your vendor")
# veg_list=['tomato','onion','carrot','brinjal']
# price_list=[20,30,60,35]
prices = {
    "Tomato": 20,
    "Onion": 30,
    "Carrot": 60,
    "Bringal": 35
}
Qty = {
    "Tomato": 1,
    "Onion": 2,
    "Carrot": 0.5,
    "Bringal": 2
}

print("Kindly type 'Know my price' to know the price of your items")
price_total=[]
def price_calc(user_input):
    if user_choice == 'Know my price':
        # for j in range(len(veg_list)): 
        #     item = float(input("How many "+veg_list[j]+"( in kg?): "))
        #     price=price_list[j]*item 
        #     print('your price =',price)
        #     price_total.append(price)
        # print(price_total)
        # total_price=sum(price_total)
        total=0
        for key in prices:
            Veg_price = prices[key] * Qty[key]
            # print(Veg_price) 
            total = total + Veg_price        
        print("The total cost is Rs",total)
        pay = float(input("Please enter an amount to pay for the fruits and vegetables: "))
        while pay < total:
            pay = float(input("Please enter an amount more than payment: "))
        change = pay - total
        print("Your change will be Rs", change)
        print('Thank you, next please')

    else:
        print('I dont know your entry, please retry')     


try:           
    while True:
        user_choice = input("Please enter your inputs: ")
        price_calc(user_choice)
except KeyboardInterrupt:
    print("User Input to stop programme")
    pass     
   
    
        

    

    


