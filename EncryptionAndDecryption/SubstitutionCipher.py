class SubstitutionCipher:
    def __init__(self, alphabet):
        """
        Initializer for the SubstitutionCipher class
        :param alphabet: Alphabet - the alphabet to use for cipher operations
        """
        self.alphabet = alphabet.alphabet
        self.ciphered_alphabet = alphabet.substitution_alphabet

    def encrypt_decrypt(self, encrypt, text):
        """
        Converts a string from alphabet_text to alphabet_convert, which encrypts or decrypts the string accordingly.
        :param encrypt: Boolean - true if the text is plaintext to be encrypted, false if the text is ciphered text
                                  to be decrypted.
        :param text: String - The text to be ciphered or deciphered.
        :return: String - Unciphered or ciphered text, depending on the text passed to the function and the value
                          of encrypt.
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
