ms = input("Enter marital status: ")
if ms == "married":
    print("Driver is Insured.")

elif ms == "unmarried":
    gender = input("Enter gender: ")
    age = int(input("Enter age: "))

    if gender == "male" and age > 30:
        print("Driver is Insured.")
    elif gender == "female" and age > 25:
        print("Driver is Insured.")
    else:
        print("Driver is Not Insured.")

else:
    print("Invalid marital status entered.")