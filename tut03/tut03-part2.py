def generate_permutations(string):
    length = len(string)
    characters = list(string)
    results = []
    stack = [0] * length

    while True:
        results.append(''.join(characters))

        for i in range(length - 1, -1, -1):
            stack[i] += 1
            if stack[i] < length - i:
                break
            stack[i] = 0
            characters[i:] = characters[i+1:] + [characters[i]]
        else:
            break

    return results

# Example Usage
string = input("Enter a string: ")
print(f"Permutations of '{string}':")
for perm in generate_permutations(string):
    print(perm)
