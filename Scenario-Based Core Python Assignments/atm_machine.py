correct_pin = "1234"  # set any PIN
attempts = 0

while attempts < 3:
    pin = input("Enter ATM PIN: ")
    if pin == correct_pin:
        print("PIN correct ✅. You can withdraw money.")
        break
    else:
        attempts += 1
        print(f"Wrong PIN! Attempts left: {3 - attempts}")

if attempts == 3:
    print("❌ Card Blocked due to 3 wrong attempts.")
