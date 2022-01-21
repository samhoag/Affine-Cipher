"""
Incomplete
"""
from EncryptionAndDecryption.Alphabet import Alphabet


class SmartCracker:
    def __init__(self, encrypted_message):
        self.alphabet = Alphabet(encrypted_message)  # can you do this? For freq. analysis you can I think.
        self.message = list(encrypted_message)
        self.msg_by_freq = self.freq_analysis()
        self.ascii_freq = list("aeorisn1tl2md0cp3hbuk45g9687yfwjvzxqASERBTMLNPOIDCHGKFJUW.!Y*@V-ZQX_$#,"
                               "/+?;^ %~=&`\)][:<(æ>\"ü|{'öä}")

    @staticmethod
    def _take_second(e):
        return e[1]

    def freq_analysis(self):
        # O(n^2)... not very efficient for longer texts
        # count all characters in the string
        chars_count = []
        for c in self.message:
            i = 0
            found = False
            while not found and i < len(chars_count):
                if c == chars_count[i][0]:
                    chars_count[i][1] += 1
                    found = True
                i += 1

            if not found:
                chars_count.append([c, 1])

        chars_count.sort(reverse=True, key=self._take_second)
        print(chars_count)

        return chars_count

    def freq_swap(self):
        print("msg by freq")
        print(self.msg_by_freq)
        for c in self.msg_by_freq:
            i = self.msg_by_freq.index(c)
            self.msg_by_freq[i][1] = self.ascii_freq[i]

        for cPair in self.message:
            c = cPair[0]
            i = -1
            for k in range(0, len(self.msg_by_freq)):
                if k == c:
                    i == k

            self.message[i] = self.msg_by_freq[i][1]

        print(self.msg_by_freq)
        print(self.message)