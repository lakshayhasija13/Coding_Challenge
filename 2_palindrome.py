def is_palindrome(input_str):
    if input_str == input_str[::-1]:
      print("palindrome")
    else :
      print("not")

input_str = input()
is_palindrome(input_str)
