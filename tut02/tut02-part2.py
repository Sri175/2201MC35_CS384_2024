def compress_string(s):
    compressed = ""
    count = 1  # Initialize the count of characters
    for i in range(1, len(s)):  # Loop through the string
        if s[i] == s[i - 1]:
            count += 1  # Increment count for consecutive characters
        else:
            compressed += s[i - 1] + str(count)  # Append character and count
            count = 1  # Reset the count
    compressed += s[-1] + str(count)  # Append the last character and count
    return compressed

# Input and output
input_string = input("Enter a string: ")
compressed_result = compress_string(input_string)
print(f"The compressed string is: {compressed_result}")
