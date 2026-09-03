import salary

basic = float(input("Enter basic salary: "))
hra = float(input("Enter HRA: "))
da = float(input("Enter DA: "))

gross = salary.gross_salary(basic, hra, da)

deduction = salary.deductions(gross)

net = salary.net_salary(gross, deduction)

print("\n--- Salary Details ---")
print("Basic Salary:", basic)
print("Gross Salary:", gross)
print("Deductions:", deduction)
print("Net Salary:", net)