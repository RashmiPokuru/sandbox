MINIMUM_LENGTH = 10
password = input(f"Password (minimum length of {MINIMUM_LENGTH}): ")
while len(password) < MINIMUM_LENGTH:
    print("Invalid Password")
    password = input(f"Password(minimum {MINIMUM_LENGTH}): ")
print("*"*len(password))
