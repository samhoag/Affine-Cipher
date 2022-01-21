from math import gcd


class AffineCipher:
    def __init__(self, key, alphabet):
        """
        Initializer for the AffineCipher class
        :param key: List containing two integers to be used as the key for the cipher. Index 0 must conform to the rules
                    confining the value of a, and index 1 must be a valid value for b.
        :param alphabet: Alphabet - the alphabet to use for the cipher operations
        """
        self.key = key
        self.alphabet = alphabet
        self.m = len(alphabet)

        if self.verify_key():
            self.a = key[0]
            self.b = key[1]
            self.a_inverse = pow(key[0], -1, self.m)

        self.int_dict = dict(zip(self.alphabet.values(), self.alphabet.keys()))

    def verify_key(self):
        """
        Verifies that a key to be used to encrypt a message with the affine cipher is a valid one. For a key to be valid,
        key[0] and the length of the alphabet being used must be coprime. Additionally, 0 < key[1] < length of alphabet.
        :return: Boolean - True if key is valid, False otherwise
        """
        # checks if a coprime with self.alphabet_len && a != 1 or 0
        if gcd(self.key[0], self.m) != 1 and 0 < self.key[0] < self.m:
            raise ValueError(
                "Key value: " + str(self.key[0]) + " is not coprime with alphabet size: " + str(self.m) +
                " or is outside of the range 0 < key value < " + str(self.m) + ".")
            return False
        # checks if b is < self.alphabet_len && b > 0
        if self.m > self.key[1] > 0:
            return True

        # returns if b value not valid.
        raise ValueError(
            "Key value: " + str(self.key[1]) + " is invalid. Select a value greater than 0 and less than " + str(
                self.m) + ".")
        return False

    def affine_cipher_encrypt(self, plaintext):
        """
        Encrypts a provided plain text message of the provided alphabet using a provided key after checking the
        key's validity.
        :param plaintext: String - The readable text to be enciphered.
        :return: String - Ciphered text
        """
        # alphabet should be a dictionary with letters as keys and ints as values
        # int_dict vice versa

        ciphered_text = ""

        for p in plaintext:
            x = self.alphabet[p]
            y = ((self.a * x) + self.b) % self.m
            ciphered_text += self.int_dict[y]

        return ciphered_text

    def affine_cipher_decrypt(self, ciphertext):
        """
        Decrypts a provided ciphered text message of the provided alphabet using a provided key.
        Key is assumed to be valid and is not checked.
        :param ciphertext: String - The ciphered text to be deciphered.
        :return: String - The deciphered plaintext
        """

        plaintext = ""

        for c in ciphertext:
            y = self.alphabet[c]
            x = (self.a_inverse * (y - self.b)) % self.m
            plaintext += self.int_dict[x]

        return plaintext
