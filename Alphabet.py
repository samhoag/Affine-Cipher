class Alphabet:
    def __init__(self, chars):
        chars = list(chars)
        self.alphabet = self._order_chars(chars)
        self.affine_alphabet = self._create_dict(self.alphabet)

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
    def _create_list(self):
        alpha_list = []
        for c in self.char:
            alpha_list.append(c)
