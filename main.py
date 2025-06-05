import string

sp_char=string.punctuation

def pass_checker(password):
    has_uppercase=False
    has_lowercase=False
    has_digits=False
    has_special=False

    if len(password)<8:
        return "Weak Password.Include more variety of characters"
    
    for char in password:
        if char.isupper():
            has_uppercase=True
        elif char.islower():
            has_lowercase=True
        elif char.isdigit():
            has_digits=True
        elif char in sp_char:
            has_special=True

    strength_pass = has_uppercase + has_lowercase + has_digits + has_special

    if(strength_pass == 4):
        return "Strong Password."
    elif(strength_pass == 3):
        return "Medium Password."
    else:
        return "Weak Password.Include more variety of characters."
    

user_password=input("Enter your password:")
result=pass_checker(user_password)

print(f"Password strength : {result}")