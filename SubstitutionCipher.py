import random


# TODO update comments
class SubstitutionCipher:
    def __init__(self, alphabet, ciphered_alphabet):
        self.alphabet = alphabet
        self.ciphered_alphabet = ciphered_alphabet

    def encrypt_decrypt(self, encrypt, text):
        """
        Converts a string from alphabet_text to alphabet_convert, which encrypts or decrypts the string accordingly.
        :param encrypt:
        :param alphabet_text: List of characters - The alphabet that the string to be converted is currently in. If the
                              string is unencrypted, this parameter should be the plain alphabet. If the string is
                              encrypted, this parameter should be the ciphered alphabet.
        :param alphabet_convert: List of characters - The alphabet that the string will be converted to. If the string is
                                 unencrypted, this parameter should be the ciphered alphabet. If the string is encrypted,
                                 this parameter should be the plain alphabet.
        :param text: String - The text to be ciphered or deciphered.
        :return: String - Unciphered or ciphered text, depending on the text passed to the function.
        """
        if encrypt:
            alphabet_text = self.alphabet
            alphabet_convert = self.ciphered_alphabet
        else:
            alphabet_text = self.ciphered_alphabet
            alphabet_convert = self.alphabet

        converted_text = ''
        # TODO see if the time complexity can be improved here. O(n^2) at the moment.
        for c in text:
            for i in range(0, len(alphabet_text)):
                if alphabet_text[i] == c:
                    converted_text += alphabet_convert[i]
                    break

        return converted_text
