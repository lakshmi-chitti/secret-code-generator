# Secret Code Generator................

# Function to encode a message
def encode_message(message, shift):
    result = ""
    for char in message:
        if char.isalpha():  # only letters
            # Uppercase letters
            if char.isupper():
                result += chr((ord(char) - 65 + shift) % 26 + 65)
            # Lowercase letters
            else:
                result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char  # keep spaces/punctuation unchanged
    return result


# Function to decode a message
def decode_message(message, shift):
    return encode_message(message, -shift)


# Function to display menu
def menu():
    while True:
        print("\n--- Secret Code Generator ---")
        print("1. Encode a message")
        print("2. Decode a message")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            msg = input("Enter the message to encode: ")
            try:
                shift = int(input("Enter shift number: "))
                print("Encoded Message:", encode_message(msg, shift))
            except ValueError:
                print(" Please enter a valid shift number.")

        elif choice == "2":
            msg = input("Enter the message to decode: ")
            try:
                shift = int(input("Enter shift number: "))
                print("Decoded Message:", decode_message(msg, shift))
            except ValueError:
                print("Please enter a valid shift number.")

        elif choice == "3":
            print("Exiting... Goodbye! ")
            break
        else:
            print(" Invalid choice. Please try again.")


# Run the program

menu()

