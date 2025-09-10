age = int(input("Enter passenger age: "))

if age < 5:
    print("Ticket is Free")
elif age <= 60:
    print("Full Ticket Price")
else:
    print("Half Ticket Price")
