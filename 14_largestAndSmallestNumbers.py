def find_largest_and_smallest(numbers):
  if not numbers:
    return None , None


  largest = small = numbers[0]

  for number in numbers[1:]:
    if largest < number:
      largest = number
    elif small > number:
      small = number

  return largest , small


numbers = [2,4,10,8,4,2,1,6,3]
large , small = find_largest_and_smallest(numbers)

print(f"Largest number is {large} and smallest number is {small}")