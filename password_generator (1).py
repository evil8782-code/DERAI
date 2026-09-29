import random
import string

def generate_initials_password(initials, total_length=16):
    """
    Generates a strong password containing the user's initials.
    """

    min_length = len(initials) + 4
    if total_length < min_length:
        total_length = min_length

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits
    special_chars = "!@#$%^&*()-_+="

    core_chars = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(numbers),
        random.choice(special_chars)
    ]

    remaining_length = total_length - len(initials) - len(core_chars)
    all_chars = lowercase + uppercase + numbers + special_chars

    for _ in range(remaining_length):
        core_chars.append(random.choice(all_chars))

    random.shuffle(core_chars)

    insert_pos = random.randint(0, len(core_chars))

    final_password = (
        "".join(core_chars[:insert_pos]) +
        initials +
        "".join(core_chars[insert_pos:])
    )

    return final_password

if __name__ == "__main__":
    user_initials = input("Enter your initials (e.g., JD): ")

    password = generate_initials_password(user_initials, 16)

    print("\n--- Password Generated ---")
    print(f"Your strong password: {password}")
