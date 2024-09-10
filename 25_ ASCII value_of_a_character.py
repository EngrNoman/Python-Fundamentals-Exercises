def ascii_value(char):
    return ord(char)

# Example usage:
character = input("Enter a character: ")

if len(character) == 1:
    print(f"The ASCII value of '{character}' is {ascii_value(character)}.")
else:
    print("Please enter a single character.")
