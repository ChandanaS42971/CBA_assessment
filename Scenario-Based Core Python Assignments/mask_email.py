email = input("Enter your email ID: ")
username, domain = email.split('@')

masked_username = username[0] + "***"
print(f"Masked Email ID: {masked_username}@{domain}")
