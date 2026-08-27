cart = []

def add_product(name, price, quantity):
    cart.append([name, price, quantity])


def remove_product(name):
    for product in cart:
        if product[0] == name:
            cart.remove(product)
            print("Product removed.")
            return

    print("Product not found.")


def subtotal():
    total = 0

    for product in cart:
        total = total + product[1] * product[2]

    return total


def coupon_discount(amount):
    if amount >= 2000:
        return amount * 0.10
    else:
        return 0


def gst(amount):
    return amount * 0.18


def invoice():
    sub = subtotal()
    discount = coupon_discount(sub)
    taxable = sub - discount
    tax = gst(taxable)
    final = taxable + tax

    print("\n----- INVOICE -----")
    print("Subtotal:", sub)
    print("Discount:", discount)
    print("GST:", tax)
    print("Final Amount:", final)


# Add products
add_product("Laptop", 50000, 1)
add_product("Mouse", 500, 2)
add_product("Keyboard", 1000, 1)

# Generate invoice
invoice()