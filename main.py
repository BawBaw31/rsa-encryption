from math import gcd


def find_e(phi):
    for i in range(2, phi):
        if gcd(i, phi) == 1:
            return i
    return None


def find_d(phi, e):
    for i in range(2, phi):
        if (i * e) % phi == 1:
            return i
    return None


def encrypt(message, public_key):
    n, e = public_key
    encrypted_message = message ** e % n
    return encrypted_message


def decrypt(encrypted_message, private_key):
    n, d = private_key
    decrypted_message = encrypted_message ** d % n
    return decrypted_message


# Generate public and private keys
p = 17
q = 23

n = p * q

phi = (p - 1) * (q - 1)

e = find_e(phi)
if e is None:
    print("No e found")
    exit(1)

d = find_d(phi, e)
if d is None:
    print("No d found")
    exit(1)

public_key = (n, e)
private_key = (n, d)

print("Public key: ", public_key)
print("Private key: ", private_key)


# User input
user_choice = input("Encrypt or decrypt? (e/d): ")

if user_choice == "e":
    message = input("Enter message to encrypt: ")
    crypted_message = ""
    for char in message:
        crypted_chars = encrypt(ord(char), public_key)
        crypted_message += str(crypted_chars) + " "
    print("Encrypted message: ", crypted_message)

elif user_choice == "d":
    crypted_message = input("Message: ")
    crypted_chars = crypted_message.split(" ")
    message = ""
    for char in crypted_chars:
        # Decryption
        decrypted_char = decrypt(int(char), private_key)
        message += chr(decrypted_char)
    print("Decrypted message: ", message)

else:
    print("Invalid choice")
