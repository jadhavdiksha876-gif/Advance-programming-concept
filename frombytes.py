from array import array

a = array('i', [45,67,90,32])

b = a.tobytes()

new_array = array('i')
new_array.frombytes(b)

print(new_array)