class ShoppingCart:
    def __init__(self, customer_name, cart_id):
        self.customer_name = customer_name
        self.cart_id = cart_id
        self.products = []

    def add_product(self, name, price):
        self.products.append([name, price])
        print("Product Added")

    def remove_product(self, name):
        for product in self.products:
            if product[0] == name:
                self.products.remove(product)
                print("Product Removed")
                return
        print("Product Not Found")

    def total_bill(self):
        total = 0
        for product in self.products:
            total += product[1]
        print("Total Bill:", total)

    def __del__(self):
        print("Shopping Cart Destroyed")

cart = ShoppingCart("Rahul", 101)

cart.add_product("Shirt", 1000)
cart.add_product("Shoes", 2000)
cart.remove_product("Shirt")
cart.total_bill()