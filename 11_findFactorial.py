# Create a program to find the factorial of a number.


def factorial(n):
  if n==0 or n==1 :
    return 1;
  else :
    return n*factorial(n-1);


number = int(input("Enter the Number: "))
result  = factorial(number);
print(f"The Factorail of the {number} is : {result}" )