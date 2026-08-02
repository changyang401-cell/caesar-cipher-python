def caesar(text, shift, encrypt=True):
    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = -shift

    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(
        alphabet + alphabet.upper(),
        shifted_alphabet + shifted_alphabet.upper()
    )

    return text.translate(translation_table)


def encrypt(text, shift):
    return caesar(text, shift)


def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)



# Caesar Cipher Program

print("===================================")
print("      CAESAR CIPHER PROGRAM")
print("===================================")
print("Choose an option:")
print("1. Encrypt a message")
print("2. Decrypt a message")
print()

choice = input("Enter 1 or 2: ").strip()

text = input("Enter your message: ")

try:
    shift = int(input("Enter the shift value (1-25): "))
except ValueError:
    print("Shift must be an integer.")
    exit()

print()

if choice == "1":
    result = encrypt(text, shift)
    print("Encrypted message:")
    print(result)

elif choice == "2":
    result = decrypt(text, shift)
    print("Decrypted message:")
    print(result)

else:
    print("Invalid option. Please run the program again and choose 1 or 2.")