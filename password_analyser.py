import re
import random
import string
import hashlib
def check_password_strength(password):
    score = 0
    remarks = []
    if len(password) >= 8:
        score += 1
    else:
        remarks.append("Password should be at least 8 characters long")
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        remarks.append("Add at least one uppercase letter")
    if re.search(r"[a-z]", password):
        score += 1
    else:
        remarks.append("Add at least one lowercase letter")
    if re.search(r"[0-9]", password):
        score += 1
    else:
        remarks.append("Include at least one number")
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        remarks.append("Add at least one special character")
    if score == 5:
        strength = "Very Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"
    return strength, remarks
def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*()"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
def save_password(hash_pwd):
    with open("password_db.txt", "a") as file:
        file.write(hash_pwd + "\n")
def is_password_reused(hash_pwd):
    try:
        with open("password_db.txt", "r") as file:
            stored = file.read().splitlines()
            return hash_pwd in stored
    except FileNotFoundError:
        return False
def main():
    password = input("Enter your password: ")
    strength, remarks = check_password_strength(password)
    print("\nPassword Strength:", strength)
    if remarks:
        print("Suggestions:")
        for r in remarks:
            print("-", r)
    hashed = hash_password(password)
    if is_password_reused(hashed):
        print("\n⚠ Warning: You have used this password before!")
    else:
        save_password(hashed)
        print("\nPassword saved successfully (not reused).")
    if strength != "Very Strong":
        print("\nSuggested Strong Password:", generate_strong_password())
if __name__ == "__main__":
    main()