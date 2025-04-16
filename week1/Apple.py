#User input to determine amount of pies needed
Amount = int(input("How many pies do you need ==> "))

#Operations to find toal amount of each ingredient
total_piecrust = 1 * Amount
total_apples = 6 * Amount
total_sugar = 0.75 * Amount
total_nutmeg = 0.125 * Amount
total_flour = 2 * Amount
total_groundcinnamon = 0.25 * Amount
total_salt = 0.25 * Amount
total_lemonjuice = 1 * Amount

#Output to display what ingredients user needs based off amount of pies planned
print(f"in order to make {Amount} pies, you will need: \n{total_piecrust} pie crust(s)\n{total_apples} apples\n{total_sugar} cups of sugar\n{total_nutmeg} teaspoons of ground nutmeg\n{total_flour} tablespoons of flour\n{total_groundcinnamon} teaspoons of cinnamon\n{total_salt} teaspons of salt\n{total_lemonjuice} tablespoons of lemon juice")