import re


email = input("What's your email address? ").strip()

if re.search(r"^[^@]+@[^@]+\.edu$",email):
    print("Valid")
else:
    print("Invalid")
