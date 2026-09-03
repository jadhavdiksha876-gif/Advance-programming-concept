file = open("transactions.txt", "w")

file.write("D,5000\n")
file.write("W,1000\n")
file.write("D,3000\n")
file.write("W,1500\n")
file.write("D,7000\n")

file.close()

file = open("transactions.txt", "r")

total_deposits = 0
total_withdrawals = 0
largest = 0

for line in file:
    data = line.strip().split(",")

    type = data[0]
    amount = int(data[1])

    if type == "D":
        total_deposits = total_deposits + amount
    else:
        total_withdrawals = total_withdrawals + amount

    if amount > largest:
        largest = amount

file.close()

balance = total_deposits - total_withdrawals

print("Total Deposits:", total_deposits)
print("Total Withdrawals:", total_withdrawals)
print("Final Balance:", balance)
print("Largest Transaction:", largest)