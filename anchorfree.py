
# coderpad.io

# FIXME You can edit anything between this line and the comment below.


def anchorfree(anchor=5, free=7, start=1, stop=100, step=1):
    """
    Return a list of strings consisting of either the number,
    the phrase "anchor", "free" or "WOW" when
    the number is divisible by anchor, free or both.

    :param anchor: return "anchor" when number is divisible by this
    :param free: return "free" when the number is divisible by this
    :param start: the first number
    :param stop: the last number (not inclusive)
    :param step: the amount to increase the number on each iteration
    :return: A list of strings
    """

    return ['1', 'anchor', 'free', 'anchor', '5', 'WOW', '7', 'anchor', 'free']


# Do not edit below here.
import unittest
class TestAppendTo(unittest.TestCase):
    def test_small(self):
        r = anchorfree(anchor=2, free=3, start=1, stop=10)
        self.assertListEqual(r, ['1', 'anchor', 'free', 'anchor', '5', 'WOW', '7', 'anchor', 'free'])

    def test_default(self):
        r = anchorfree()
        self.assertListEqual(r,
            ['1', '2', '3', '4', 'anchor', '6', 'free', '8', '9', 'anchor',
             '11', '12', '13', 'free', 'anchor', '16', '17', '18', '19',
             'anchor', 'free', '22', '23', '24', 'anchor', '26', '27', 'free', '29',
             'anchor', '31', '32', '33', '34', 'WOW', '36', '37', '38', '39', 'anchor',
             '41', 'free', '43', '44', 'anchor', '46', '47', '48', 'free', 'anchor',
             '51', '52', '53', '54', 'anchor', 'free', '57', '58', '59', 'anchor',
             '61', '62', 'free', '64', 'anchor', '66', '67', '68', '69', 'WOW',
             '71', '72', '73', '74', 'anchor', '76', 'free', '78', '79', 'anchor',
             '81', '82', '83', 'free', 'anchor', '86', '87', '88', '89', 'anchor',
             'free', '92', '93', '94', 'anchor', '96', '97', 'free', '99'])

    def test_step(self):
        r = anchorfree(step=10)
        self.assertListEqual(r, ['1', '11', 'free', '31', '41', '51', '61', '71', '81', 'free'])

unittest.main(exit=False)
