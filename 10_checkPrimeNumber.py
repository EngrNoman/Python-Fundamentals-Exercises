# Write a Python program to check if a number is a prime number.

number = int(input("Enter the Number:"))

is_prime = True 

if number <=0 :
  is_prime = False
else :
  for i in range(2 , number):
    if number % i == 0:
      is_prime = False
      break



if is_prime:
  print("Number is Prime")
else:
  print("Number is Not Prime")