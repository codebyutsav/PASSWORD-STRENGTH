# 🔐 Password Strength Checker

A simple Python script to check the strength of a password based on the use of uppercase, lowercase, digits, and special characters.

![Password Strength Visual](https://i.ytimg.com/vi/iJ01q-sRJAw/maxresdefault.jpg)

## 📋 Features

- Checks if the password:
  - Has **uppercase** letters
  - Has **lowercase** letters
  - Includes **digits**
  - Contains **special characters**
- Categorizes password strength into:
  - **Strong** ✅
  - **Medium** ⚠️
  - **Weak** ❌

## 🧠 Logic

- Password must be at least **8 characters long**
- The more variety of characters used, the stronger the password

## 🖥️ Usage

Run the script and input your password when prompted:

```
Enter your password: MyPass@123  
Password strength : Strong Password.
```

## 📦 Requirements

- Python 3.x
- Uses built-in `string` module (no extra installation needed)

## 🚀 How to Run

1. Clone the repository or copy the code
2. Run the script using Python:

```
python pass_checker.py
```

## 💡 Note

This is a **basic level** checker and not suitable for production-level password validation. For more secure validation, consider additional factors like dictionary checks, entropy calculations, etc.
