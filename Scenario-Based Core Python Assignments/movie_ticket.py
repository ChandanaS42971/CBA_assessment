time = int(input("Enter show time in 24hr format (e.g., 15 for 3 PM): "))
ticket_price = 200  # base price

if time < 17:
    discount = ticket_price * 0.30
    final_price = ticket_price - discount
    print(f"Matinee Show 🎬: Final Ticket Price = ₹{final_price}")
else:
    print(f"Evening Show 🎬: Ticket Price = ₹{ticket_price}")
