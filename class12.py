class FoodOrder:
    def __init__(self, order_id, customer_name, food_item, quantity, price):
        self.order_id = order_id
        self.customer_name = customer_name
        self.food_item = food_item
        self.quantity = quantity
        self.price = price

    def total_bill(self):
        total = self.quantity * self.price
        tax = total * 0.05
        return total + tax

    def __del__(self):
        print("Order Completed")

o = FoodOrder(101, "Priya", "Pizza", 2, 300)

print("Order ID:", o.order_id)
print("Customer:", o.customer_name)
print("Food:", o.food_item)
print("Total Bill:", o.total_bill())