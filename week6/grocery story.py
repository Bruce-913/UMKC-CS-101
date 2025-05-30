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

    def store_display(self):
        print(f"User placed order from:\nStore: {self.store_name}\nLocation: {location}")
        pass

    def display_products(self):
        print("The following items are available at this store:")
        for product, price in self.products_available.items():
            print(f"{product}: ${price:.2f}")

class Cart:
    def __init__(self, store):
        self.store = store
        self.cart_products = {}
        # self.receipt = receipt

    def added_item(self, product_name, product_quantity):
        self.cart_products[product_name] = product_quantity

    def remove_item(self, product_name, product_quantity):
        if product_name in self.cart_products:
            self.cart_products[product_name] -= product_quantity
            if  self.cart_products[product_name] <= 0:
                del self.cart_products[product_name]
                print(f"Deleted {product_name} out of your cart.")
            else:
                print(f"Item {product_name} not found inside your cart.")

    def receipt(self):
        total_price = 0
        for product_name,product_quantity in self.cart_products.items():
            price_per_item = store.products_available.get(product_name) * product_quantity

            total_price += price_per_item
        return total_price
            
    def cart_description(self):
        print("Your cart contains:")
        for product_name, product_quantity in self.cart_products.items():
            print(f"- {product_name} with quantity: {product_quantity}")
        print(f"Total receipt is ${self.receipt():.2f}")


if __name__ == "__main__":
    store_name = input("Welcome! Which store would you like to visit today?")

    location = input("Which location are you buying from:")

    store = Store(store_name, location)

    store.display_products()

    cart = Cart(store)

    while True:
        product_name = input("Enter name of product you would like:").capitalize()
        if product_name in store.products_available.keys():
            store.products_available.get(product_name)
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

    cart.added_item(product_name, product_quantity)
    cart.cart_description()
    
    while True:
        removal_permission = input("Would you like to remove an item y/n").lower()
        if removal_permission == "y":
            while True:
                removed_item = input("Enter name of which product you would like to remove:").capitalize()
                if removed_item in cart.cart_products.keys():
                    while True:
                        try:
                            removed_quantity = int(input("Enter the amount of the product you would like to remove:"))
                            break
                        except ValueError:
                            print("Incorrect value enter a non-decimal number less than or equal to amount in cart")
                    cart.remove_item(removed_item, removed_quantity)
                    cart.cart_description()
                    break
                else:
                    print("Item is not in your cart, try again")
        else:
            break
    
    while True:
        adding_permission = input("Would you like to add another item y/n").lower()
        if adding_permission == "y":
            while True:
                add_product_name = input("Enter name of product you would like to add:").capitalize()
                if add_product_name in store.products_available.keys():
                    store.products_available.get(add_product_name)
                    break
                else:
                    print(f"{add_product_name} is not an item available, try again")
        
            while True:
                try:
                    add_product_quantity = int(input("Enter the amount you would like of this product:"))
                    if add_product_quantity <= 0:
                        print("Invalid number, try again")
                    else:
                        break
                except ValueError:
                    print("Invalid entry, try again")
            
            cart.added_item(add_product_name, add_product_quantity)
            cart.cart_description()
        else:
            break
    cart.cart_description()
    print("Thanks for shopping!")