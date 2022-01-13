"""
Programming Project 1: Affine Cipher Implementation
Author: Sam Hoag
Date: January 12, 2022
Instructor: Dr. Cutter

This program provides functions to encrypt and decrypt a string using the affine cipher and a provided key.
"""




from math import gcd


def affine_cipher_verify_key(key, alphabet_len):
    """
    Verifies that a key to be used to encrypt a message with the affine cipher is a valid one. For a key to be valid,
    key[0] and the length of the alphabet being used must be coprime. Additionally, 0 < key[1] < length of alphabet.
    :param key: List of 2 integers to check
    :param alphabet_len: Integer - the length of the alphabet
    :return: Boolean - True if key is valid, False otherwise
    """
    # checks if a coprime with alphabet_len && a != 1 or 0
    if gcd(key[0], alphabet_len) != 1 and 0 < key[0] < alphabet_len:
        print("Key value: " + str(key[0]) + " is not coprime with alphabet size: " + str(alphabet_len) +
              " or is outside of the range 0 < key value < " + str(alphabet_len) + ".")
        return False
    # checks if b is < alphabet_len && b > 0
    if alphabet_len > key[1] > 0:
        return True

    # returns if b value not valid.
    print("Key value: " + str(key[1]) + " is invalid. Select a value greater than 0 and less than " + str(
        alphabet_len) + ".")
    return False


def affine_cipher_encrypt(key, alphabet_dict, plaintext):
    """
    Encrypts a provided plain text message of the provided alphabet using a provided key after checking the
    key's validity.
    :param key: List of 2 integers - Integer at index 0 must be coprime with the length of the alphabet. Integer at
                index 1 must be greater than 0 and less than the length of the alphabet (0 < key[1] < alphabet length)
    :param alphabet_dict: Dictionary - Contains char letters as keys and corresponding integers as values.
                          !!! The same alphabet must be used for encryption and decryption !!!
    :param plaintext: String - The readable text to be enciphered.
    :return: String - Ciphered text
    """
    # alphabet should be a dictionary with letters as keys and ints as values
    # int_dict vice versa
    m = len(alphabet_dict)
    good_key = affine_cipher_verify_key(key, m)
    if not good_key:
        return None
    plaintext = plaintext.lower()

    int_dict = dict(zip(alphabet_dict.values(), alphabet_dict.keys()))
    ciphered_text = ""
    a = key[0]
    b = key[1]

    for p in plaintext:
        x = alphabet_dict[p]
        y = ((a * x) + b) % m
        ciphered_text += int_dict[y]

    return ciphered_text


def affine_cipher_decrypt(key, alphabet_dict, ciphertext):
    """
    Decrypts a provided ciphered text message of the provided alphabet using a provided key.
    Key is assumed to be valid and is not checked.
    :param key: List of 2 integers
    :param alphabet_dict: Dictionary - Contains char letters as keys and corresponding integers as values.
                          !!! The same alphabet must be used for encryption and decryption !!!
    :param ciphertext: String - The ciphered text to be deciphered.
    :return: String - The deciphered plaintext
    """
    m = len(alphabet_dict)
    int_dict = dict(zip(alphabet_dict.values(), alphabet_dict.keys()))
    ciphertext = ciphertext.lower()
    plaintext = ""
    a_inverse = pow(key[0], -1, m)
    b = key[1]

    for c in ciphertext:
        y = alphabet_dict[c]
        x = (a_inverse * (y - b)) % m
        plaintext += int_dict[x]

    return plaintext


def main():
    """
    Main function for the program.
    For the time being, edit alpha_dict to edit the alphabet, edit k to alter the key used to encipher,
    and edit text to edit the plaintext to be enciphered.
    TODO: Set up user input
    """
    alpha_dict = {
        "a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11, "m": 12,
        "n": 13, "o": 14, "p": 15, "q": 16, "r": 17, "s": 18, "t": 19, "u": 20, "v": 21, "w": 22, "x": 23, "y": 24,
        "z": 25, " ": 26, ".": 27, ",": 28, ";": 29
    }
    k = [23, 2]
    text = "Whatsoever therefore is consequent to a time of Warre, where every man " \
           "is Enemy to every man; the same is consequent to the time, wherein men " \
           "live without other security, than what their own strength, and their " \
           "own invention shall furnish them withall. In such condition, there is " \
           "no place for Industry; because the fruit thereof is uncertain; and " \
           "consequently no Culture of the Earth; no Navigation, nor use of the " \
           "commodities that may be imported by Sea; no commodious Building; no " \
           "Instruments of moving, and removing such things as require much force; " \
           "no Knowledge of the face of the Earth; no account of Time; no Arts; no " \
           "Letters; no Society; and which is worst of all, continuall feare, and " \
           "danger of violent death; And the life of man, solitary, poore, nasty, " \
           "brutish, and short."

    print("plaintext in: " + text)
    ciphered = affine_cipher_encrypt(k, alpha_dict, text)
    print("ciphered text: " + ciphered)
    print("plaintext out: " + affine_cipher_decrypt(k, alpha_dict, ciphered))


if __name__ == '__main__':
    main()
