def total_bill(prices, quantities):
    total = 0
    for i in range(len(prices)):
        total = total + prices[i] * quantities[i]
    if total >= 1000:
        discount = total * 0.10
    else:
        discount = 0
    final_bill = total - discount
    return final_bill
prices = [200, 300, 500]
quantities = [2, 1, 1]
print("Total bill:", total_bill(prices, quantities))