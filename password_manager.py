import random
import string
import os

# Change Master Password to yours
MASTER_PASSWORD = "Your Master Password"


def create_character_list():
    """Create and return the base character set"""
    return (string.ascii_lowercase + string.ascii_uppercase +
            string.digits + string.punctuation + ' ')


def generate_and_store_keys():
    """Generate 10 shuffled keys ONLY if keys.txt doesn't exist"""
    if not os.path.exists('keys.txt'):
        base_chars = create_character_list()
        with open('keys.txt', 'w') as f:
            for _ in range(10):
                shuffled = list(base_chars)
                random.shuffle(shuffled)
                f.write(''.join(shuffled) + '\n')
        print("Generated new keys.txt with 10 shuffled keys.")
    else:
        print("Using existing keys.txt (safe from overwriting).")


def encrypt_password(password, key_num):
    """Encrypt password using the specified key number (0-9)"""
    with open('keys.txt', 'r') as f:
        keys = f.readlines()
        key = keys[key_num].strip()

    base_chars = create_character_list()
    encrypted = []

    for char in password:
        if char in base_chars:
            index = base_chars.index(char)
            encrypted.append(key[index])
        else:
            encrypted.append(char)  

    return ''.join(encrypted) + str(key_num)


def decrypt_password(encrypted_password):
    """Decrypt password using the key number stored as last character"""
    if not encrypted_password:
        return ""

    key_num = int(encrypted_password[-1])
    encrypted = encrypted_password[:-1]  

    with open('keys.txt', 'r') as f:
        keys = f.readlines()
        key = keys[key_num].strip()

    base_chars = create_character_list()
    decrypted = []

    for char in encrypted:
        if char in key:
            index = key.index(char)
            decrypted.append(base_chars[index])
        else:
            decrypted.append(char)

    return ''.join(decrypted)


def verify_master_password():
    """Ask for master password before revealing passwords"""
    attempt = input("Enter master password to continue: ")
    return attempt == MASTER_PASSWORD


def main():
    generate_and_store_keys()  # Safe key initialization

    while True:
        print("\n=== Password Manager ===")
        print("1. Store new password")
        print("2. Retrieve password")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            website = input("Enter website name: ")
            password = input("Enter password: ")

            key_num = random.randint(0, 9)
            encrypted = encrypt_password(password, key_num)

            with open('passwords.txt', 'a') as f:
                f.write(f"website: {website}\n")
                f.write(f"password: {encrypted}\n\n")

            print(f"Password for {website} stored securely!")

        elif choice == '2':
            if not verify_master_password():
                print("Incorrect master password. Access denied.")
                continue

            website = input("Enter website name to retrieve password: ")
            found = False

            try:
                with open('passwords.txt', 'r') as f:
                    lines = f.readlines()

                    for i, line in enumerate(lines):
                        if line.startswith(f"website: {website}"):
                            encrypted_line = lines[i+1]
                            encrypted = encrypted_line.split(": ")[1].strip()
                            decrypted = decrypt_password(encrypted)
                            print(f"\nPassword for {website}: {decrypted}")
                            found = True
                            break
            except FileNotFoundError:
                pass

            if not found:
                print("No password found for this website.")

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try 1, 2, or 3.")


if __name__ == "__main__":
    main()
