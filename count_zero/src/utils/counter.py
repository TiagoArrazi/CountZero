from difflib import SequenceMatcher


class Counter:

    @classmethod
    def count_zeros(cls, string):
        try:
            zero_string = ''.join(['0' for i in range(len(string))])
        except TypeError:
            return None

        matcher = SequenceMatcher(None, string, zero_string)
        match = matcher.find_longest_match(0, len(string), 0, len(zero_string))

        return match.size
