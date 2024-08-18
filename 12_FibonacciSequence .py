# Write a program to generate a Fibonacci sequence up to n terms.


def fibonacci(n):
  sequence = []
  a , b = 0 , 1
  for _ in range(n):
    sequence.append(a)
    a ,b = b , a+b 
  
  return sequence


number = int(input("Enter the NUmber: "))
result = fibonacci(number)
print(f"Fibonacci S  {result}")

