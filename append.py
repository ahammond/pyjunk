
# coderpad.io

# FIXME You can edit anything between this line and the comment below.
def append_to(element, to=[]):
    """
    Append an element to a list.
    If not list provided, create a new list containing only the element.

    :param element: the thing to append
    :param to: the list to append it to
    :return: the list with the appended thing
    """

    to.append(element)
    return to

# Do not edit below here.
import unittest
class TestAppendTo(unittest.TestCase):
    def test_default(self):
        r = append_to('a')
        self.assertListEqual(r, ['a'])

    def test_no_default(self):
        l = ['a', 'b']
        r = append_to('c', l)
        self.assertListEqual(r, ['a', 'b', 'c'])

    def test_both(self):
        r = append_to('b')
        append_to('c', r)
        self.assertListEqual(r, ['b', 'c'])


unittest.main(exit=False)
