print("__________PASSWORD CHECKER________")

while True:
    password = input("\nEnter your password: ")

    length_ok = len(password) >= 8
    upper_ok = any(char.isupper() for char in password)
    lower_ok = any(char.islower() for char in password)
    digit_ok = any(char.isdigit() for char in password)
    special_ok = any(char in "!@#$%^&*()-_=+{}[];:',./?<>~`" for char in password)
    score = sum([length_ok, upper_ok, lower_ok, digit_ok, special_ok])

    if score == 5:
        strength = "Very Strong Password"
    elif score == 4:
        strength = "Strong Password"
    elif score == 3:
        strength = "Moderate Password"
    else:
        strength = "Weak Password"

    print("\n🔐 Password Strength: ", strength)
    print("🔎 Details:")
    print("✓ Length is at least 8 characters" if length_ok else "✗ Length is less than 8 characters")
    print("✓ Contains at least one UPPERCASE letter" if upper_ok else "✗ Missing an UPPERCASE letter")
    print("✓ Contains at least one lowercase letter" if lower_ok else "✗ Missing a lowercase letter")
    print("✓ Contains at least one digit" if digit_ok else "✗ Missing a digit")
    print("✓ Contains at least one special character" if special_ok else "✗ Missing a special character")

    choice = input("\nWould you like to check another password? (yes/no): ").strip().lower()
    if choice not in ['yes', 'y']:
        print("\nThank you for using the Password Checker. Stay safe!")
        break
