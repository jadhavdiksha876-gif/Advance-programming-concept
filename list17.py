matrix1 = []
matrix2 = []
result = []

print("Enter elements of First Matrix:")
for i in range(3):
    row = []
    for j in range(3):
        num = int(input())
        row.append(num)
    matrix1.append(row)

print("Enter elements of Second Matrix:")
for i in range(3):
    row = []
    for j in range(3):
        num = int(input())
        row.append(num)
    matrix2.append(row)

for i in range(3):
    row = []
    for j in range(3):
        row.append(matrix1[i][j] + matrix2[i][j])
    result.append(row)

print("\nResultant Matrix:")
for row in result:
    print(row)