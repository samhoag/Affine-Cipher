from math import gcd


def affine_cipher_verify_key(key, alphabet_len):
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
