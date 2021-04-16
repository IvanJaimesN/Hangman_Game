def get_database():
    words_db = []
    with open("./data.txt", "r", encoding="utf-8") as f:
        for word in f:
            words_db.append(word)
    return words_db

def normalize_character(character):
    import unicodedata
    """Replace accentuated characters by their non-accentuated counterparts

    A simple way to do this would be to decompose accentuated characters in the
    sequence using one of the unicode decomposition schemes and then filter the
    resulting sequence to remove combining characters (also known as
    diacritical marks).

    Comments: the following solution is a very naive implementation of that
    only uses basic operations on the sequence of unicode characters.

    A more efficient approach that works only for languages that use the
    latin alphabet would use batch conversion to ASCII characters as done in:

        sklearn.feature_extraction.text.strip_accents_ascii
    Source: https://www.programcreek.com/python/?CodeExample=remove+accents
    """
    text = unicodedata.normalize('NFKD', character)
    return "".join([c for c in text if not unicodedata.combining(c)]) 