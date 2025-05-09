class House:
    def __init__(self, year_built, purchase_price, current_year, house_location,):
        self.year_built = year_built
        self.purchase_price = purchase_price
        self.current_year = current_year
        self.house_location = house_location

    def __str__(self):
        return f"year built: {self.year_built}\nPurchase Price: {self.purchase_price}\nCurrent year: {self.current_year}\nHouse Location: {self.house_location}"

    def calculating_current_value(self):
        current_value = self.purchase_price*(1+0.08)**(self.current_year - self.year_built)
        return current_value

    def money_earned(self):
        total_money = self.calculating_current_value() - self.purchase_price
        return total_money 

if __name__ == "__main__":
    year_built = 0
    purchase_price = 0
    current_year = 0
    house_location = "N/A"

    print("Welcome to the house calculation app")
    while True:
        try:
            while True:
                try:
                    year_built = int(input("What year was this house built in?"))
                    if year_built <= 0 or len(str(year_built)) < 4 :
                        print("Year built must be a positive number with 4 digits.")
                        continue
                    else:
                        break
                except ValueError:
                    print("Invalid input. Please enter a valid year.")
            while True:
                try:
                    purchase_price = float(input("How much money did you buy this house for?"))
                    if purchase_price <= 0:
                        print("Purchase price must be a positive number.")
                        continue
                    else:
                        break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            while True:
                try:
                    current_year = int(input("What year is it currently:"))
                    if current_year <= 0 or current_year < year_built:
                        print("Year built must be a positive number and greater than or equal to year built.")
                        continue
                    else:
                        break
                except ValueError:
                    print("Invalid input. Please enter a valid year.")
            house_location = input("Where is this house located at?")
            house = House(year_built, purchase_price, current_year, house_location)

            calculated_current_value = house.calculating_current_value()
            money_earned = house.money_earned()

            print(f"\nHouse Information:\n   Year built: {year_built}\n   Purchase Price: {purchase_price:.2f}\n   Current value of the house: ${calculated_current_value:.2f}\n   House location:{house_location}")
            print(f"\nTotal Value earned:\n${money_earned:.2f}")

            retry = input("Would you like to check the price of another house? y/n").lower()
            if retry == "y" :
                continue
            elif retry == "n":
                break
            else:
                print("Invalid entry, try again")
        except:
            ValueError("Wrong, try again")    