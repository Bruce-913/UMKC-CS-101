# import math

def order():
    Chipotle_Menu = {
    "Chicken Burrito": 7.95,
    "Steak Burrito Bowl": 9.30,
    "Chicken Quesadilla": 8.50
    }

    Q39_Menu = {
    "Wings": 7.95,
    "Burnt End Burger": 16.50,
    "Brisket": 12.99
    }

    print("Welcome to 101 delivery")
    print("We deliver food from the following 2 restaurants:\n1- Chipotle \n2- Q39 \n3- Both restaurants")

    while True:
        try:
            choice = int(input("Enter your choice of restaurant: \n1 for Chipotle \n2 for Q39 \n3 for both\nChoice:"))
            if choice == 1:
                for item, price in Chipotle_Menu.items():
                    print (f"{item} - ${price:.2f}")
                break
            elif choice == 2:
                for item, price in Q39_Menu.items():
                    print (f"{item} - ${price:.2f}")
                break
            elif choice == 3:
                for item, price in Chipotle_Menu.items():
                    print (f"{item} - ${price:.2f}")
                break
            else:
                print("Invalid entry, type 1, 2, or 3 to see your menu.")
        except ValueError:
            print("Invalid entry. Try again")
    food_choice = int(input("What select food would you like from this menu? 1/2/3:"))
    # if food_choice == 1:
#this next line should include what item on the menu to get

#The line after that should include the quantity of the item

#Then display current price of order and ask user if they want to add any more
#   

order()
# def delivery_fee():



