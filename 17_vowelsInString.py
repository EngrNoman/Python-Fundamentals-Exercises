# Create a program to count the number of vowels in a string.


def vowel_in_string(str):
  vowelStr = "aeiouAEIOU"
  count = 0 
  for char in str:
    if char in vowelStr:
      count +=1
  
  return count 


input_String = str(input("Enter the String:"))
print(f"NUmber in Vowel: {vowel_in_string(input_String)}")