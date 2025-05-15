# 1- Create an instance of Cart class.
# 2- Ask the user for the store name and location.
# 3- Display the products available in your store.
# 4- Ask the user to choose the products and the quantity.
# 5- Below is a sample of the output

class Store:
    def __init__(self, location, product_name):
        self.products_available = {
            "Milk":2.50,
            "Bread": 1.98,
            "Egg": 0.70,
            "Flour": 1.18,
            "Oil":4.00,
            "Cheese": 2.68
        }
        self.location = location
        self.product_name = product_name

class Cart:
    def __init__(self, product_name, product_quantity, receipt):
        self.cart_products = {}
        self.product_name = product_name
        self.product_quantity = product_quantity
        self.receipt = receipt
        pass

    def added_item(self, name, price):
        self.cart_products[name] = price
        pass

    def remove_item(self, name):
        del self.cart_products[name]
        pass

if __name__ == "__main__":
    store = Store()
    cart = Cart()
    specific_store = input("Welcome! Which store would you like to visit today?")

