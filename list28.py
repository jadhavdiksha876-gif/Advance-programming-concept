scores = []
for i in range(10):
    score = int(input("Enter score of match " + str(i + 1) + ": "))
    scores.append(score)

highest = max(scores)
lowest = min(scores)
total = sum(scores)
average = total / len(scores)

century = 0
half = 0

for score in scores:
    if score >= 100:
        century += 1
    elif score >= 50:
        half += 1

print("\nHighest Score:", highest)
print("Lowest Score:", lowest)
print("Total Runs:", total)
print("Average Runs:", average)
print("Centuries:", century)
print("Half-Centuries:", half)