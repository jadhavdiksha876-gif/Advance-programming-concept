y=int(input("Enter The Year:"))
if y%4==0 and y%100!=0 or y%400==0:
    print("the year is leap year.")
else:
    print("Year is not leap year.")