# Write a Python program to find the GCD (Greatest Common Divisor) of two numbers.


def gcd(a , b):
  while b!=0:
    a , b = b , a%b
  
  return a

num1 = int(input("Enter the First Number:"))
num2 = int(input("Enter the Second Number:"))

result = gcd(num1 , num2)
print(f"The GCD of {num1} and {num2} is {result}.")
