balance = float(input("Enter initial bank balance: "))
interest_rate = 0.05

for month in range(1, 13):
    balance += balance * interest_rate
    print(f"Month {month}: Balance = {balance:.2f}")
