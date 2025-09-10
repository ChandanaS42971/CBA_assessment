# Restaurant bill program with GST
cost = float(input("Enter the cost of the item: "))
gst = cost * 0.18
final_amount = cost + gst

print("\n----- Restaurant Bill -----")
print(f"Base cost: ₹{cost:.2f}")
print(f"GST (18%): ₹{gst:.2f}")
print(f"Final amount: ₹{final_amount:.2f}")
print("---------------------------")
