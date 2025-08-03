def check_palindrome(str):
    
    clean_str=str.lower().replace(" ", "")
    
    reverse_str=clean_str[::-1]
    return clean_str == reverse_str



str=input("Enter a string  ")
if check_palindrome(str):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")