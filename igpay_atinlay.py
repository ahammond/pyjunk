import unittest


def pig_latin(input):
    """
    Given a phrase, return that phrase, translated to pig latin.

    RULES:
    1) For words that begin with consonant sounds,
    all letters before the initial vowel are placed at the end of the word sequence.
    Then, "ay" is added. Example:
    pig -> igpay

    2) When words begin with consonant clusters (multiple consonants that form one sound),
    the whole sound is added to the end. Example:
    smile -> ilesmay

    3) For words that begin with vowel sounds, one just adds "way". Example:
    eat -> eatway

    4) Capitalization should be preserved. Example:
    "This is a Sentence" -> "Isthay isway away Entencesay"

    5) Punctuation should be preserved.
    Whitespace may either be normalized or preserved.
    Example:
    "pig,  latin!" -> "igpay, atinlay!"

    :param input: the string to transalate
    :return: the translated string
    """

    return 'igpay'


class TestAppendTo(unittest.TestCase):

    def test_single_consonant(self):
        r = pig_latin('pig')
        self.assertEqual(r, 'igpay')

unittest.main(exit=False)
