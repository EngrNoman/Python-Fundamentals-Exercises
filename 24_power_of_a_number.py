  # Write a Python program to calculate the power of a number

def power(base , exponent):
  result = 1
  for i in range(abs(exponent)):
    result *= base
  if exponent <0:
    return 1/result
  return result

base = float(input("Enter the Base Value : "))
exponent = int(input("Enter the Exponent : "))
power_result = power(base , exponent)
print(power_result)