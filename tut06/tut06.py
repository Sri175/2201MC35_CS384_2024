def main():
    # Define allowed numbers and symbols
    allowed_numbers = set(map(int, input("Enter allowed numbers (space-separated): ").split()))
    allowed_symbols = {'@', '&', '%'}
    
    while True:
        password = input("Enter Your Password: ")
        
        # Check length
        if len(password) < 8:
            print("Too Short. Password must be at least 8 characters long.")
            continue

        # Initialize categories
        lowercase, uppercase, digits, symbols = [], [], [], []
        valid = True

        # Validate each character
        for char in password:
            if char.islower():
                lowercase.append(char)
            elif char.isupper():
                uppercase.append(char)
            elif char.isdigit():
                digits.append(char)
                if int(char) not in allowed_numbers:
                    valid = False
                    print(f"Invalid Number: {char}")
            else:
                symbols.append(char)
                if char not in allowed_symbols:
                    valid = False
                    print(f"Invalid Symbol: {char}")

        # Check for missing categories
        if not lowercase:
            print("Add lowercase letters to your password.")
            valid = False
        if not uppercase:
            print("Add uppercase letters to your password.")
            valid = False
        if not digits:
            print("Add some numbers to your password.")
            valid = False
        if not symbols:
            print("Add at least one symbol (@, &, or %).")
            valid = False

        # Final validation
        if valid:
            print("Password Saved!")
            break

    print(f"Your password is: {password}")

if __name__ == "__main__":
    main()
