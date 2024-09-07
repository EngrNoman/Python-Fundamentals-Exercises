# Write a Python program to check if a number is an Armstrong number.


def ArmStrong_number(number):
  num_str = str(number)
  num_digits = len(num_str)

  total = sum(int(digit)**num_digits for digit in num_str)

  return total == number



number = int(input("Enter the Number:"))

if ArmStrong_number(number):
  print(f"{number} is AramStrong ")
else:
  print(f"{number} is Not AramStrong ")
