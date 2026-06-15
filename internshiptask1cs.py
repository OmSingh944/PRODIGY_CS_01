import string

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


def brute_force(text):
    print("\nPossible Decryptions:")
    for shift in range(1, 26):
        print(f"Shift {shift}: {decrypt(text, shift)}")


def save_to_file(content):
    with open("output.txt", "a") as file:
        file.write(content + "\n")
    print("✅ Saved to output.txt")


def main():
    while True:
        print("\n===== Caesar Cipher Tool =====")
        print("1. Encrypt Message")
        print("2. Decrypt Message")
        print("3. Brute Force Attack")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice in ['1', '2']:
            message = input("Enter message: ")
            try:
                shift = int(input("Enter shift value (0-25): ")) % 26
            except ValueError:
                print("❌ Invalid shift! Enter a number.")
                continue

            if choice == '1':
                result = encrypt(message, shift)
                print("🔐 Encrypted:", result)
            else:
                result = decrypt(message, shift)
                print("🔓 Decrypted:", result)

            save = input("Save result to file? (y/n): ").lower()
            if save == 'y':
                save_to_file(result)

        elif choice == '3':
            message = input("Enter encrypted message: ")
            brute_force(message)

        elif choice == '4':
            print("Exiting... धन्यवाद!")
            break

        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()