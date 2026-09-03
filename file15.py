file = open("cosine.py", "r")
new_file = open("new.py", "w")
for line in file:
    if not line.strip().startswith("#"):
        new_file.write(line)
file.close()
new_file.close()
print("Comments removed successfully.")