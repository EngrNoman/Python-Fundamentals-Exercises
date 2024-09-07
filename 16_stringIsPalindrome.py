# Write a Python program to check if a string is a palindrome.


def palindrome(s):
  cleaned_str = " ".join(e for e in s if e.isalnum()).lower()

  return cleaned_str == cleaned_str[::-1]



input_str = input(str("Enter the String "));
if palindrome(input_str):
  print("String is Palindrome")
else:
  print("String is not Palindrome")