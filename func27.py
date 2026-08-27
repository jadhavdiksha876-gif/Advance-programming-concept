def consultation_charges():
    return 500

def laboratory_charges():
    return 1000

def medicine_charges():
    return 1500

def room_charges(days):
    return days * 1000

def discount(category, total):
    if category == "senior":
        return total * 0.20
    elif category == "child":
        return total * 0.10
    else:
        return 0

def final_bill(category, days):
    consultation = consultation_charges()
    laboratory = laboratory_charges()
    medicine = medicine_charges()
    room = room_charges(days)

    total = consultation + laboratory + medicine + room
    discount_amount = discount(category, total)

    final = total - discount_amount

    return final

category = input("Enter patient category (senior/child/normal): ")
days = int(input("Enter room days: "))

print("Final Hospital Bill: ₹", final_bill(category, days))