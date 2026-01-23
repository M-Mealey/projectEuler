"""
Project Euler Problem 59
========================

Each character on a computer is assigned a unique code and the preferred
standard is ASCII (American Standard Code for Information Interchange).
For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to
ASCII, then XOR each byte with a given value, taken from a secret key. The
advantage with the XOR function is that using the same encryption key on
the cipher text, restores the plain text; for example, 65 XOR 42 = 107,
then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text
message, and the key is made up of random bytes. The user would keep the
encrypted message and the encryption key in different locations, and
without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified
method is to use a password as a key. If the password is shorter than the
message, which is likely, the key is repeated cyclically throughout the
message. The balance for this method is using a sufficiently long password
key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three
lower case characters. Using cipher1.txt, a file containing the encrypted
ASCII codes, and the knowledge that the plain text must contain common
English words, decrypt the message and find the sum of the ASCII values
in the original text.
"""
from collections import Counter
from itertools import product

# space + the five most common letters in English.
# The most common byte for each key is very likely the encoded version of one of these
most_common_chars = [' ', 'e', 't', 'a', 'o', 'i']

bytes = []
with open('resources/cipher1.txt') as f:
    data = f.read()
    bytes = [int(x) for x in data.split(',')]

bytes_by_key = {1: [], 2: [], 3: []}
for x in range(len(bytes)):
    bytes_by_key[x%3 + 1].append(bytes[x])

# given a byte list where all bytes are encrypted by the same key,
# find the most common byte and return list of potential keys that would
# correspond to this byte being one of the most common characters
def get_likely_keys(b_list):
    byte_count = Counter(b_list)
    most_common_byte = byte_count.most_common(1)[0][0]
    # problem states valid cipher chars are lowercase letters
    likely_keys = [ord(c) ^ most_common_byte for c in most_common_chars if ord('z') >= (ord(c)^most_common_byte) >= ord('a')]
    return likely_keys

k1 = get_likely_keys(bytes_by_key[1])
k2 = get_likely_keys(bytes_by_key[2])
k3 = get_likely_keys(bytes_by_key[3])
# in practice there's only one possible key for each list, but if there were more this would generate all combinations
possible_key_combos = list(product(k1, k2, k3))

# validate the plaintext by checking if at least 9 of first 10 words are common English words
# using the word list from https://public.websites.umich.edu/~jlawler/wordlist.html
# return True if passes, False if not
def validate_message(txt):
    with open('resources/wordlist.txt') as f:
        words = f.read().split('\n')
    first_ten_words = txt.split(" ")[:10]
    valid_words = [w for w in first_ten_words if w.lower() in words]
    if len(valid_words) >= 9:
        return True
    return False

# trys to decrypt the plaintext with the given keys. Returns plaintext if it passes validation,
# or None if it doesn't
def try_decrypt(keys):
    decrypted_bytes = [bytes[x] ^ keys[x%3] for x in range(len(bytes))]
    decoded_string = ''.join([chr(x) for x in decrypted_bytes])
    if validate_message(decoded_string):
        return decoded_string
    else:
        return None

def try_keys(key_combos):
    for k in key_combos:
        if try_decrypt(k):
            return try_decrypt(k)
    return None

plaintext = try_keys(possible_key_combos)
if not plaintext:
    print("ERROR: COULD NOT DECRYPT")
ascii_sum = sum([ord(c) for c in plaintext])
print(ascii_sum)

