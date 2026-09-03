file1 = open("fil1.txt", "r")
file2 = open("fil2.txt", "r")

line_number = 0
different = False

while True:
    line1 = file1.readline()
    line2 = file2.readline()

    if line1 == "" and line2 == "":
        break

    line_number = line_number + 1

    if line1 != line2:
        print("Files are different.")
        print("First difference is at line:", line_number)
        print("File 1:", line1.strip())
        print("File 2:", line2.strip())

        different = True
        break

file1.close()
file2.close()

if different == False:
    print("Files are identical.")