# 1- Create an instance of Cart class.
# 2- Ask the user for the store name and location.
# 3- Display the products available in your store.
# 4- Ask the user to choose the products and the quantity.
# 5- Below is a sample of the output

# The Store class will include the following:
# - One setter method: to set the name and the location.?

# The Cart class will include the following:
# - Four instance attributes:
# o Receipt

class Store:
    def __init__(self, store_name, location):
        self.products_available = {
            "Milk":2.50,
            "Bread": 1.98,
            "Egg": 0.70,
            "Flour": 1.18,
            "Oil":4.00,
            "Cheese": 2.68
        }
        self.location = location
        self.store_name = store_name

    def set_store(self):
        pass

    def store_display(self):
        print(f"User placed order from:\nStore: {self.store_name}\nLocation: {location}")
        pass

    def display_products(self):
        print("The following items are available at this store:")
        for product, price in self.products_available.items():
            print(f"{product}: ${price}")

class Cart:
    def __init__(self, product_name, product_quantity, receipt):
        self.cart_products = {}
        self.product_name = product_name
        self.product_quantity = product_quantity
        self.receipt = receipt

    def added_item(self, product_name, product_quantity):
        self.cart_products[product_name] = product_quantity

    def remove_item(self, name):
        if name in self.cart_products:
            del self.cart_products[name]
            print(f"Deleted {name} out of your cart.")
        else:
            print(f"book {name} not found inside your cart.")

if __name__ == "__main__":
    store_name = input("Welcome! Which store would you like to visit today?")

    location = input("Which location are you buying from:")

    store = Store(store_name, location)

    store.display_products()

    while True:
        product_name = input("Enter name of product you would like:").capitalize()
        if product_name in store.products_available.keys():
            break
        else:
            print(f"{product_name} is not an item available, try again")

    while True:
        try:
            product_quantity = int(input("Enter the amount you would like of this product:"))
            if product_quantity <= 0:
                print("Invalid number, try again")
            else:
                break
        except ValueError:
            print("Invalid entry, try again")
    print(product_name)
    # receipt = store.products_available.values
    # cart = Cart()
    # cart.added_item(product_name, product_quantity)
    # print(cart.cart_products)
