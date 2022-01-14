"""
Programming Project 1: Affine/Substitution Cipher Implementation
Author: Sam Hoag
Date: January 12, 2022
Instructor: Dr. Cutter

This program provides functions to encrypt and decrypt a string using the affine and substitution ciphers and a provided key.
"""
import random
import string

from AffineCipher import AffineCipher
from Alphabet import Alphabet
from SubstitutionCipher import SubstitutionCipher


def affine_cipher_test(alphabet, key, text):
    """
    For testing the affine cipher.
    Prints plain, ciphered, and deciphered text.

    :param alphabet: Dictionary[character, integer] - The alphabet of the text to be used for the cipher and
                                                      corresponding integer values
    :param key: List of 2 Integers - Values to be used as the key. Ensure they comply with the rules of the
                                     affine cipher.
    :param text: String - The text to be used for the cipher.
    """
    affine_cipher = AffineCipher(key, alphabet)

    ciphered = affine_cipher.affine_cipher_encrypt(text)

    print("Plaintext in: " + text)
    print("Ciphered text: " + ciphered)
    print("Deciphered out: " + affine_cipher.affine_cipher_decrypt(ciphered))


def substitution_cipher_test(alphabet, text):
    """
    For testing the substitution cipher.
    Prints plain alphabet, ciphered alphabet, plaintext, ciphered, and deciphered text.

    :param alphabet: List of characters - The alphabet of the text to be used for the cipher
    :param text: String - The text to be used for the cipher
    """
    substitution_cipher = SubstitutionCipher(alphabet.alphabet, alphabet.substitution_alphabet)

    ciphered_text = substitution_cipher.encrypt_decrypt(True, text)
    deciphered_text = substitution_cipher.encrypt_decrypt(False, ciphered_text)

    print("Plain alphabet in: " + str(alphabet.alphabet))
    print("Ciphered alphabet out: " + str(alphabet.substitution_alphabet))
    print("Plaintext in: " + text)
    print("Ciphered text out: " + ciphered_text)
    print("Ciphered text in: " + ciphered_text)
    print("Plaintext out: " + deciphered_text)


def main():
    """
    Main function for the program.
    For the time being, edit alpha_dict to edit the alphabet, edit k to alter the key used to encipher,
    and edit text to edit the plaintext to be enciphered.
    """

    # For use with the affine cipher
    affine_alphabet = {
        "a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11, "m": 12,
        "n": 13, "o": 14, "p": 15, "q": 16, "r": 17, "s": 18, "t": 19, "u": 20, "v": 21, "w": 22, "x": 23, "y": 24,
        "z": 25, " ": 26, ".": 27, ",": 28, ";": 29
    }
    affine_key = [23, 2]

    # For use with the substitution cipher
    substitution_alphabet = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F',
                             'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L',
                             'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R',
                             's', 'S', 't', 't', 'T', 'u', 'U', 'v', 'V', 'w', 'W', 'x',
                             'X', 'y', 'Y', 'z', 'Z', '1', '2', '3', '4', '5', '6', '7',
                             '8', '9', ' ', '.', '[', ']', ',', ';', '-', '!', '?']

    substitution_alphabet_simple = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                                    'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    text_simple = "hello world."
    hobbes = "Whatsoever therefore is consequent to a time of Warre, where every man " \
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

    alphabet_source_string = '`1234567890-=qwertyuiop[]asdfghjkl;"' + "'zxcvbnm,./!@#$%^&*()_+QWERTYUIOP{" \
                                                                      "}|ASDFGHJKL:ZXCVBNM<>? "

    alphabet = Alphabet(alphabet_source_string)

    print("=============================")
    print("Affine Cipher Test")
    print("-----------------------------")
    affine_cipher_test(alphabet.affine_alphabet, affine_key, hobbes)
    print("=============================")
    print("Substitution Cipher Test")
    print("-----------------------------")
    substitution_cipher_test(alphabet, hobbes)


if __name__ == '__main__':
    main()
