# Write a Python program to convert a decimal number to binary

def decimal_to_binary(n):
  if n==0:
    return "0";


  binary = "";

  while n>0:
    binary += str(n % 2) 
    n=n//2

  return binary

decimal_number = int(input("Enter a decimal number :"))
binary_representation = decimal_to_binary(decimal_number)
print(f"{decimal_number} into Binary is : {binary_representation}")
    
