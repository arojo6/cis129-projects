#Alondra Rojo 
# CIS 129 10/01/2024

# Declare Variables and constants for this program 
NumberOfCoffeePurchased = 0
NumberOfMuffinPurchased = 0
coffee = 5.00
muffin = 4.00
tax = 0.06
taxprice = 0


def Main():
    # Declare Variables and constants for this program 
    NumberOfCoffeePurchased = 0
    NumberOfMuffinPurchased = 0
    coffee = 5.00
    muffin = 4.00
    tax = 0.06
    taxprice = 0

    # Declare menu
    print(" ")
    print("Hello! welcome to forosix bakery.")
    print("We are currently serving hot coffee and freshly baked muffins")
    print(" ")

    # Ask user for item being purchased
    NumberOfCoffeePurchased = int(input('How many coffees would you like? ')) 
    NumberOfMuffinPurchased = int(input('How many Muffins would you like? ')) 
    
    # calculate cost of items without taxes
    CostOfCoffee = NumberOfCoffeePurchased * coffee
    CostOfMuffin = NumberOfMuffinPurchased * muffin

    # calculate total cost and taxes
    taxprice = (CostOfMuffin + CostOfCoffee) * tax
    totalcost = taxprice + (CostOfCoffee + CostOfMuffin)

    # print out recipt
    print("***************************************")
    print("My Coffee and Muffin Shop")
    print("Number of coffees bought?")
    print(NumberOfCoffeePurchased)
    print("Number of muffins bought?")
    print(NumberOfMuffinPurchased)
    print("***************************************")
    print("")
    print("***************************************")
    print("My Coffee and Muffin Shop Receipt")
    print(NumberOfCoffeePurchased, "Coffee at $5 each:", CostOfCoffee)
    print(NumberOfMuffinPurchased, "Muffins at $4 each:", CostOfMuffin)
    print("6% tax: ", taxprice)
    print("---------")
    print("Total: $", totalcost)
    print("***************************************")

Main()
