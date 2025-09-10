patient_id = input("Enter patient ID: ")

if patient_id.startswith("HOSP"):
    print("Valid patient ID.")
else:
    print("Invalid patient ID. Must start with 'HOSP'.")
