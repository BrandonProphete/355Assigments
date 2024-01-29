# Queens College
# Internet and Web Technology  (CSCI 355)
# Winter 2024
# Assignment 8b - Encryption and Decryption
# Brandon Prophete
# Worked with Class
from numpy import random
import numpy as np
import rsa

# [1] Choose a text file and simplify it as follows:
# Convert any lowercase characters to uppercase characters
# Remove anything that is not (after step a) an uppercase character (A-Z), digit (0-9), space or period.
# Your character set will now be of size 38 (26 + 10 + 2) which will simplify your substitution cipher in the next steps.

# [2] Randomly choose a substitution cipher, that is a random permutation of the 38 elements of your character set. (See Ch. 8, Slide 12 - except we have 38 characters instead of just 26.)  You can use np.random.permutation to generate the permutation.
def sub_cipher(alphabet):
    return random.permutation(alphabet)

# [3] Use RSA to securely send the one-time substitution cipher (i.e. the permutation) from the client to the server. The client will be aware of the server’s “public key”. You can see the basics of using RSA in Python in Slide 13 of our supplement “LT_NetworkSecurity”. More details, if required, can be found on the Internet, including
# the official Python-RSA homepage at https://stuvel.eu/software/rsa/
# An elaborate example from TutorialPoint at https://bit.ly/2K6oWHh
def encrypt(text, cipher):
    return ''.join([cipher[ord(c)-65] for c in text])

def decrypt(text, cipher):
    return ''.join([chr(cipher.index(c)+ 65) for c in text])

def encrypt_rsa(cipher, pub_key):
    cipher = cipher.encode('utf-8')
    encrypted_cipher = rsa.encrypt(cipher, pub_key)
    return encrypted_cipher

def get_keys():
    return rsa.newkeys(2048)

def decrypt_rsa(encrypted_cipher, priv_key):
    return rsa.decrypt(encrypted_cipher, priv_key).decode('utf-8')

def read_file(filename):
    with open(filename) as f:
        return f.read()

def write_file(file_name, text):
    with open(file_name, "w") as f:
        f.write(text)
def main():
    text = read_file('Assignment8d.txt')
    alphabet = [chr(ord("A") + i) for i in range(26)]

    cipher = sub_cipher(alphabet)
    encrypted_text = encrypt(text, cipher)

    write_file('Assignment8e2.txt', encrypted_text)
    decrypted_text = decrypt(encrypted_text, cipher.tolist())
    print(decrypted_text)

    pub_key, priv_key = get_keys()
    encrypted_cipher = encrypt_rsa(",".join(cipher.tolist()), pub_key)
    print("This is the encrypted cipher: ", encrypted_cipher)

    decrypted_cipher = decrypt_rsa(encrypted_cipher, priv_key)
    print("This is the decrypted cipher: ", decrypted_cipher)


if __name__ == "__main__":
        main()