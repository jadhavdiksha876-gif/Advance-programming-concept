temp = []

for i in range(30):
    t = float(input("Enter temperature of day " + str(i + 1) + ": "))
    temp.append(t)

highest = max(temp)
lowest = min(temp)
average = sum(temp) / len(temp)

above = 0
below = 0

for t in temp:
    if t > average:
        above += 1
    elif t < average:
        below += 1

print("\nHottest Day Temperature:", highest)
print("Coldest Day Temperature:", lowest)
print("Average Temperature:", average)
print("Days Above Average:", above)
print("Days Below Average:", below)