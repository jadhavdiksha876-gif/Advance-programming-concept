file = open("attendance.txt", "w")

file.write("101,Amit,70,100\n")
file.write("102,Priya,85,100\n")
file.write("103,Rahul,60,100\n")
file.write("104,Neha,90,100\n")

file.close()


file = open("attendance.txt", "r")

print("Students having attendance below 75%:")

for line in file:
    data = line.strip().split(",")

    roll = data[0]
    name = data[1]
    attended = int(data[2])
    total = int(data[3])

    percentage = (attended / total) * 100

    if percentage < 75:
        print(roll, name, percentage, "%")

file.close()