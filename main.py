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


def substitution_cipher_build_ciphered_alphabet(raw_alphabet):
    """
    Creates a substitution-ciphered alphabet from the provided un-ciphered alphabet.
    Alphabet is ciphered by randomly popping indices from the plain alphabet and appending them to the ciphered alphabet
    :param raw_alphabet: List of characters - the alphabet from which to create the ciphered alphabet
    :return: List of characters - the ciphered alphabet.
    """
    plain_alphabet = raw_alphabet.copy()
    ciphered_alphabet = []

    while len(plain_alphabet) > 0:
        ciphered_alphabet.append(plain_alphabet.pop(random.randint(0, len(plain_alphabet) - 1)))

    return ciphered_alphabet


def substitution_cipher_encrypt_decrypt(alphabet_text, alphabet_convert, text):
    """
    Converts a string from alphabet_text to alphabet_convert, which encrypts or decrypts the string accordingly.
    :param alphabet_text: List of characters - The alphabet that the string to be converted is currently in. If the
                          string is unencrypted, this parameter should be the plain alphabet. If the string is
                          encrypted, this parameter should be the ciphered alphabet.
    :param alphabet_convert: List of characters - The alphabet that the string will be converted to. If the string is
                             unencrypted, this parameter should be the ciphered alphabet. If the string is encrypted,
                             this parameter should be the plain alphabet.
    :param text: String - The text to be ciphered or deciphered.
    :return: String - Unciphered or ciphered text, depending on the text passed to the function.
    """
    # text = text.lower()
    converted_text = ''
    # TODO see if the time complexity can be improved here. O(n^2) at the moment.
    for c in text:
        for i in range(0, len(alphabet_text)):
            if alphabet_text[i] == c:
                converted_text += alphabet_convert[i]
                break

    return converted_text


def substitution_cipher_encrypt(plain_alphabet, plaintext):
    """
    This function should not be used. Use substitution_cipher_encrypt_decrypt() instead.
    It is only here to provide a clearer understanding of how substitution encryption works.
    """
    plaintext = plaintext.lower()
    ciphered_alphabet = substitution_cipher_build_ciphered_alphabet(plain_alphabet)
    ciphered_text = ''
    for c in plaintext:
        for i in range(0, len(plain_alphabet)):
            if plain_alphabet[i] == c:
                ciphered_text += ciphered_alphabet[i]
                break
    return [ciphered_text, ciphered_alphabet]


def substitution_cipher_decrypt(ciphered_alphabet, plain_alphabet, ciphered_text):
    """
    This function should not be used. Use substitution_cipher_encrypt_decrypt() instead.
    It is only here to provide a clearer understanding of how substitution decryption works.
    """
    plaintext = ''
    for c in ciphered_text:
        for i in range(0, len(ciphered_alphabet)):
            if ciphered_alphabet[i] == c:
                plaintext += plain_alphabet[i]

    return plaintext


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

    ciphered_alpha_list = substitution_cipher_build_ciphered_alphabet(alphabet)
    ciphered_text = substitution_cipher_encrypt_decrypt(alphabet, ciphered_alpha_list, text)
    deciphered_text = substitution_cipher_encrypt_decrypt(ciphered_alpha_list, alphabet, ciphered_text)

    print("Plain alphabet in: " + str(alphabet))
    print("Ciphered alphabet out: " + str(ciphered_alpha_list))
    print(" ")
    print("Plaintext in: " + text)
    print("Ciphered text out: " + ciphered_text.rstrip())
    print("")
    print("Ciphered text in:" + ciphered_text)
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

    # Does not always work perfectly because the cipher sometimes is such that a special string character is
    # generated. For this reason, \, ', and " were removed. Whenever these characters are found in the plaintext,
    # they are simply ignored. Additionally, the original text contains "returns" that are not represented by \n,
    # meaning there are some words with no spaces.
    # Only works if DoI.txt is in the same directory as this file.
    jefferson = open("DoI.txt").read()

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
    # substitution_cipher_test(substitution_alphabet, jefferson)


if __name__ == '__main__':
    main()
