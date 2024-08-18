# Write a Python program to reverse a string.

def reverseString(value):
  return value[::-1]


originalString = "Noman Mahmood Ahmad"
newString = reverseString(originalString)

print(f"Original string: {originalString}")
print(f"Reversed string: {newString}")