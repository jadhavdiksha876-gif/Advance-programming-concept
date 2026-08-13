patients = (
    (101, "Diksha", 25, "A+"),
    (102, "Sneha", 30, "B+"),
    (103, "Amit", 45, "O+"),
    (104, "Priya", 28, "A+"),
    (105, "Seeta", 35, "O-")
)
print("All Patient Records:")
for patient in patients:
    print(patient)

search_id = 103
found = False

for patient in patients:
    if patient[0] == search_id:
        print("\nPatient Found:", patient)
        found = True

if not found:
    print("\nPatient not found")

print("\nTotal number of patients =", len(patients))

blood_group = "A+"

print("\nPatients with blood group", blood_group, ":")
for patient in patients:
    if patient[3] == blood_group:
        print(patient)