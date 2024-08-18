# Write a program to sum all the elements in a list.


def sum_of_list(numbers):
  total = 0
  for i in numbers:
    total+=i
  return total


my_list = [1,1,1,1,1]
result = sum_of_list(my_list)
print(f"sum is {result}")