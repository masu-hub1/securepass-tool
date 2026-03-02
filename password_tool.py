import random
import string


def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Include numbers.")

    if any(char in string.punctuation for char in password):
        score += 1
    else:
        feedback.append("Include special characters (!@#$...).")

    if score <= 2:
        strength = "Weak"
    elif score == 3 or score == 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, feedback


def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    while True:
        print("\n🔐 SecurePass Tool")
        print("1. Check Password Strength")
        print("2. Generate Strong Password")
        print("3. Exit")

        choice = input("Choose an option (1/2/3): ")

        if choice == "1":
            password = input("Enter your password: ")
            strength, feedback = check_password_strength(password)

            print(f"\nPassword Strength: {strength}")
            if feedback:
                print("Suggestions:")
                for item in feedback:
                    print("-", item)

        elif choice == "2":
            try:
                length = int(input("Enter desired password length (default 12): ") or 12)
                password = generate_strong_password(length)
                print(f"\nGenerated Password: {password}")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "3":
            print("Goodbye 👋")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
