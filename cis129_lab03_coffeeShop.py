#Alondra Rojo 
# CIS 129 10/01/2024


def Main():
    # Declare Variables and constants for this program 
    NumberOfCoffeePurchased = 0
    NumberOfMuffinPurchased = 0
    NumberOfCookiesPurchased = 0
    NumberOfMatchasPurchased = 0
    coffee = 5.00
    muffin = 4.00
    matcha = 5.00
    cookie = 3.00
    tax = 0.06
    taxprice = 0

    # Declare menu
    print(" ")
    print("Hello! welcome to forosix bakery. (-_-)")
    print("We are currently serving hot coffee, delicious matcha, freshly made cookies and muffins")
    print(" ")

    # instructions 
    print('I really encourage you trying one of every of our items as they are made with love!! :D')
    print("please enter an integer only")
    # Ask user for item being purchased
    NumberOfCoffeePurchased = int(input('How many Coffees would you like? ')) 
    NumberOfMuffinPurchased = int(input('How many Muffins would you like? ')) 
    NumberOfCookiesPurchased = int(input('How many Cookies would you like? ')) 
    NumberOfMatchasPurchased = int(input('How many Matchas would you like? ')) 
    
    # calculate cost of items without taxes
    CostOfCoffee = NumberOfCoffeePurchased * coffee
    CostOfMuffin = NumberOfMuffinPurchased * muffin
    CostOfCookies = NumberOfCookiesPurchased * cookie
    CostOfMatcha = NumberOfMatchasPurchased * matcha
    
    # calculate total cost and taxes
    taxprice = (CostOfMuffin + CostOfCoffee + CostOfCookies + CostOfMatcha) * tax
    totalcost = taxprice + CostOfCoffee + CostOfMuffin + CostOfCookies + CostOfMatcha
    formattedtaxprice = float(f'{taxprice:.2f}')
    formattedtotalcost = float(f'{totalcost:.2f}')

    # print out recipt
    print("")
    print("Thank you for visiting Forosix bakery!! Here is your recipt.")
    print("")
    print("")
    print("***************************************")
    print("Forosix Bakery")
    print("Number of coffees bought?")
    print(NumberOfCoffeePurchased)
    print("Number of muffins bought?")
    print(NumberOfMuffinPurchased)
    print("Number of matcha bought?")
    print(NumberOfMatchasPurchased)
    print("Number of cookies bought?")
    print(NumberOfCookiesPurchased)
    print("***************************************")
    print("")
    print("***************************************")
    print("My Coffee and Muffin Shop Receipt")
    print(NumberOfCoffeePurchased, "Coffee at $5 each:", CostOfCoffee)
    print(NumberOfMuffinPurchased, "Muffins at $4 each:", CostOfMuffin)
    print(NumberOfCookiesPurchased, "Muffins at $4 each:", CostOfCookies)
    print(NumberOfMatchasPurchased, "Coffee at $5 each:", CostOfMatcha)
    print("6% tax: ", formattedtaxprice)
    print("---------")
    print("Total: $", formattedtotalcost)
    print("***************************************")

Main()
