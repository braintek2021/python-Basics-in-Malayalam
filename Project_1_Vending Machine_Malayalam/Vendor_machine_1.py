##Per litre price
Milk_price=50
curd_price=30

print ("Welcome to the Python Vending Machine.")
# Asking User on type of product.

item = input("Would you like to buy Milk,Curd or Both: ")
if item == 'Milk': 
    print("Thank you for the selection")
    milk_qty = int(input("Kindly enter the quantity in liters: "))
    milk_cost = milk_qty*Milk_price
    print("Kindly enter Rupees "+str(milk_cost)+" below" )
    cus_paid=int(input("Kindly enter the amount to be paid: "))
    if cus_paid==milk_cost:
        print("Thank you, please collect " + item)
elif item == 'Curd': 
    print("Thank you for the selection. you have selected "+ item+" for purchase")
    curd_qty = int(input("Kindly enter the quantity in liters: "))
    curd_cost = curd_qty*curd_price
    print("Kindly enter Rupees "+str(curd_cost)+" below" )
    cus_paid=int(input("Kindly enter the amount to be paid: "))
    if cus_paid==curd_cost:
        print("Thank you, please collect " + item)
    else:
        print("Wrong entry,Please check")             
elif item == 'Both': 
    print("Thank you for the selection. you have selected "+ item+"milk and curd for purchase")
    milk_qty = int(input("Kindly enter the Milk quantity in liters: "))
    milk_cost = milk_qty*Milk_price
    curd_qty = int(input("Kindly enter the Curd quantity in liters: "))
    curd_cost = curd_qty*curd_price
    Total_cost =curd_cost+milk_cost
    print("Kindly enter Rupees "+str(Total_cost)+" below" )
    cus_paid=int(input("Kindly enter the amount to be paid: "))
    if cus_paid==Total_cost:
        print("Thank you, please collect " + item)
    else:
        print("Wrong entry,Please check")
else: 
    print("I dont know your entry, please make the correct entry")