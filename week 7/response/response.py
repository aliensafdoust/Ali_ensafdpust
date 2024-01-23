import validators

Add_ress = input("What/'s your email address? ").strip()

# checking Email address

if validators.email(Add_ress):
    print("Valid")
else:
    print("Invalid")
