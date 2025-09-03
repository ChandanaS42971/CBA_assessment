# Online store discount system
purchase = float(input("Enter total purchase amount: "))

if purchase > 5000:
    discount = purchase * 0.20
else:
    discount = purchase * 0.10

final_price = purchase - discount

print("\n----- Bill -----")
print(f"Purchase amount: ₹{purchase:.2f}")
print(f"Discount applied: ₹{discount:.2f}")
print(f"Final amount: ₹{final_price:.2f}")
print("----------------")
