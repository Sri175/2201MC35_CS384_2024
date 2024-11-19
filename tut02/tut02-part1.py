def unitary_sum_of_digits(n):
    n = abs(n)  # Ensure the number is positive
    while n >= 10:  # Continue until a single digit is obtained
        sum_digits = 0
        temp = n
        while temp > 0:
            sum_digits += temp % 10  # Get the last digit
            temp //= 10  # Remove the last digit
        n = sum_digits  # Update n to the sum of its digits
    return n

# Input and output
number = int(input("Enter an integer: "))
result = unitary_sum_of_digits(number)
print(f"The Unitary Sum of Digits of {number} is: {result}")
