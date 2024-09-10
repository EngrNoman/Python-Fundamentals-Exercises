# Write a Python program to find the LCM (Least Common Multiple) of two numbers.

def gcd(a,b):
  while b:
    a , b = b, a%b
  
  return a

def lcm(a,b):
  return (a*b)// gcd(a,b)

num1 = int(input("Enter the 1st  number: "))
num2 = int(input("Enter the 2st  number: "))

lcm_result = lcm(num1 , num2)

print(f"The LCM of {num1} and {num2} is {lcm_result}")
           