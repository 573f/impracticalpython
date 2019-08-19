"""Load a text file as a list

Arguments:
- text file name (and directory path, if needed)

Exceptions:
- IOError if filename not found.

Returns:
- A list of all words in a text file in lowercase.

Requires-import sys

"""
import sys


def load(file):
    """Open a text file and return a list of lowercase strings."""
    try:
        with open(file) as in_file:
            loaded_txt = in_file.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as err:
        print("{}\nError opening {}. Terminating program."
              .format(err, file), file=sys.stderr)
        sys.exit(1)
