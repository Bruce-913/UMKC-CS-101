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
        pass

class Cart:
    def __init__(self, product_name, product_quantity):
        self.products = {}
        pass
    # def added_item():