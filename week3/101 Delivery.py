Chipotle_Menu = {
    "Chicken Burrito": 7.95,
    "Steak Burrito Bowl": 9.30,
    "Chicken Quesadilla": 8.50,
    "Rice Bowl": 12.99
    }

Q39_Menu = {
    "Wings": 7.95,
    "Burnt End Burger": 16.50,
    "Brisket": 12.99
    }

Mcdonalds = {
    "Big Mac": 6.00,
    "Fries": 2.00,
    "Chicken Nuggets": 9.00
}

restaurants = {
    "Chipotle": Chipotle_Menu,
    "Q39": Q39_Menu,
    "Mcdonalds": Mcdonalds
}

def Fees(subtotal):
    if subtotal >= 35:
        print("Your total is greater or equal to 35, you have free delivery!")
    else:
        subtotal += 10
        print("Because your total is under $35, you will have a $10 delivery fee.")

    final_total = subtotal * (1 + 4.3 / 100)
    print(f"Your final total after fees and taxes will be ${final_total:.2f}")

def print_menu(menu):
    for x,(item, price) in enumerate(menu.items(), start=1):
        print (f"{x}- {item} - ${price:.2f}")

def quantity():
    while True:
        try:
            total_item = int(input("How many would you like?"))
            if total_item <= 0:
                print("Please enter a number greater than 0.")
            else:
                break
        except ValueError:
            print("Invalid entry. Please enter a number.")
    return total_item

def main():
    print("Welcome to 101 delivery")
    print("We deliver food from the following:")
    print()
    for x,(restaurant) in enumerate(restaurants.keys(), start=1):
        print (f"{x}- {restaurant}")
    while True:
        try:
            num_choice = int(input("Enter your choice of restaurant:"))
            if num_choice > len(restaurants) or num_choice <= 0:
                print("Invalid entry. Try again")
                continue

            rest_choice = list(restaurants)[num_choice-1]
            break
        except ValueError:
            print("Invalid entry. Try again")
    #print(restaurant)
    #print(restaurants[rest_choice])
    orderTotal = restaurant_order(rest_choice, restaurants[rest_choice])
    Fees(orderTotal)

def restaurant_order(rest_name, rest_menu):
    print_menu(rest_menu)
    subtotal = 0
    while True:
        try:
            food_choice = int(input(f"What food would you like from {rest_name}"))

            if food_choice > len(rest_menu) or food_choice <= 0:
                print("Invalid Entry. Try again.")
                continue

            item = list(rest_menu.values())[food_choice-1]
            total_item = quantity()

            net_price = total_item * item
            subtotal = subtotal + net_price
            print(f"your current total from this menu is ${subtotal:.2f}")
            extra = input("Would you like to add any other item from this menu? y/n").lower()
            if extra == "y":
                continue
            elif extra == "n":
                break
            else:
                print("Invalid entry")
        except ValueError:
            print("Invalid Entry. Try again")
    return subtotal

main()