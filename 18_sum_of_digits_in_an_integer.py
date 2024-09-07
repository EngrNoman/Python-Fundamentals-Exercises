# Write a Python program to find the sum of digits in an integer.

def sum_of_digit(number):
  number = abs(number)
  total = 0 
  while number > 0:
    total += number % 10
    number //= 10
  
  return total

number = int(input("Enter the NUmber "))
print(f"Sum of Digits: {sum_of_digit(number)}")