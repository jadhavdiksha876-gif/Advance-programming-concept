from array import array

a = array('i', [89,67,43,56])

f = open("data.txt", "wb")
a.tofile(f)
f.close()

print("Data written to file")