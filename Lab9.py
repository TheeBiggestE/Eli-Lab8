#Eli Davis's Encoder file

def encode(password):
    encoded_password = ""
    for digit in password:
        encoded_digit = (int(digit) + 3) % 10
        encoded_password += str(encoded_digit)
    return encoded_password


def main():
    while True:
        print("\nMenu:")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        choice = input("Please enter an choice: ")

        if choice == '1':
            password = input("Enter the 8-digit password to encode: ")
            if len(password) != 8 or not password.isdigit():
                print("Invalid password. Please enter an 8-digit password containing only integers.")
                continue
            encode(password)
            print("Your password has been encoded and stored!")
        elif choice == '2':
            print(f"The encoded password is {encode(password)}, and the original password is {decode(password)}")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

# Call the main function to start the program
if __name__ == "__main__":
    main()