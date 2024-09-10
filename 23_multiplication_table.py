# Write a Python program to print the multiplication table of a given number


def table(n, up_to =10):
  print(f"The Table of {n}")
  for i in range(1,up_to+1):
    print(f"{n} * {i} = {n*i}")


number = int(input("Enter a number: "))
table(number)
