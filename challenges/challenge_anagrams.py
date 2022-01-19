def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    if (first_string or second_string) in (None, ''):
        return False
    else:
        # já que o bubbleSort não deu certo...
        """
        url longa: https://stackoverflow.com/questions/48217471/
        is-it-possible-to-check-for-anagram-without-using-sorted-or-dictionary-that-pe
        """
        def build_counters(string):
            counter = {}
            for letter_index in string:
                counter[letter_index] = counter.setdefault(letter_index, 0) + 1
            return counter
    fsthash = build_counters(first_string)
    sndhash = build_counters(second_string)

    return fsthash == sndhash
