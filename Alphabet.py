import random


class Alphabet:
    def __init__(self, chars):
        chars = list(chars)
        self.alphabet = self._order_chars(chars)
        self.affine_alphabet = self._create_dict(self.alphabet)
        self.substitution_alphabet = self._create_substitution_alphabet(self.alphabet)

    @staticmethod
    def _order_chars(chars):
        """
        Reorders list of unordered chars according to their ASCII code.
        :return: ordered list
        """
        # Initializes a list of size 94, the total number of ASCII characters.
        ordered = [None] * 94
        for c in chars:
            # checks for duplicates
            if not (c in ordered):
                ordered[ord(c) - 32] = c

        return list(filter(None, ordered))

    @staticmethod
    def _create_dict(alphabet):
        alpha_dict = {}
        v = 0
        for c in alphabet:
            alpha_dict[c] = v
            v += 1
        return alpha_dict

    @staticmethod
    def _create_substitution_alphabet(alphabet):
        """
        Creates a substitution-ciphered alphabet from the provided un-ciphered alphabet.
        Alphabet is ciphered by randomly popping indices from the plain alphabet and appending them to the ciphered alphabet
        :param raw_alphabet: List of characters - the alphabet from which to create the ciphered alphabet
        :return: List of characters - the ciphered alphabet.
        """
        plain_alphabet = alphabet.copy()
        ciphered_alphabet = []

        while len(plain_alphabet) > 0:
            ciphered_alphabet.append(plain_alphabet.pop(random.randint(0, len(plain_alphabet) - 1)))

        return ciphered_alphabet
