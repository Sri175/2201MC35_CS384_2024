def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_rotations(number):
    rotations = []
    num_str = str(number)
    for i in range(len(num_str)):
        rotated = num_str[i:] + num_str[:i]
        rotations.append(int(rotated))
    return rotations

def is_rotational_prime(number):
    rotations = get_rotations(number)
    for rotation in rotations:
        if not is_prime(rotation):
            return False
    return True

# Example Usage
number = int(input("Enter a number: "))
if is_rotational_prime(number):
    print(f"{number} is a Rotational prime.")
else:
    print(f"{number} is not a Rotational prime.")
