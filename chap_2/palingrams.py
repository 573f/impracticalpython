"""Find all word-pair palingrams in a dictionary file."""
import load_dictionary

WORD_LIST = load_dictionary.load('/usr/share/dict/web2')


# find word-pair palingrams
def find_palingrams():
    """Find dictionary palingrams."""
    pali_list = []
    words = set(WORD_LIST)
    for word in words:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end-i] and rev_word[end-i:] in words:
                    print('.', end='', flush=True)
                    pali_list.append((word, rev_word[end-i:]))
                if word[:i] == rev_word[end-i:] and rev_word[:end-i] in words:
                    print('.', end='', flush=True)
                    pali_list.append((rev_word[:end-i], word))
    return pali_list

PALINGRAMS = find_palingrams()
PALINGRAMS_SORTED = sorted(PALINGRAMS)

# display list of palingrams
print("\n\nNumber of palingrams found = {}\n".format(len(PALINGRAMS_SORTED)))
for first, second in PALINGRAMS_SORTED:
    print("{} {}".format(first, second))
