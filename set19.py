morning = {"Amit", "Rahul", "Sneha", "Priya", "Neha"}
afternoon = {"Priya", "Neha", "Rohan", "Kiran", "Amit"}
print("Students present in both sessions:", morning & afternoon)
print("Students only in morning:", morning - afternoon)
print("Students only in afternoon:", afternoon - morning)
print("Students present in at least one session:", morning | afternoon)