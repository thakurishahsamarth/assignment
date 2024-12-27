user_input = input("Enter a string: ")
letters = 0
digits = 0
spaces = 0
for char in user_input:
    if char.isalpha(): 
        letters += 1
    elif char.isdigit():  
        digits += 1
    elif char.isspace(): 
        spaces += 1
print("Letters:", letters)
print("Digits:", digits)
print("Spaces:", spaces)
