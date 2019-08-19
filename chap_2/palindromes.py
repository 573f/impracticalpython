"""Find palindromes in a dictionary file."""
import load_dictionary

WORD_LIST = load_dictionary.load('/usr/share/dict/web2')
PALI_LIST = []

for word in WORD_LIST:
    if len(word) > 1 and word == word[::-1]:
        PALI_LIST.append(word)

print("\nNumber of palindromes found = {}\n".format(len(PALI_LIST)))
print(*PALI_LIST, sep=', ')
