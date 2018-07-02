
# coderpad.io

# FIXME You can edit anything between this line and the comment below.
def append_to(element, to=[]):
    """
    Append an element to a list.
    If no list is provided, create a new list containing only the element.

    :param element: the thing to append
    :param to: the list to append it to
    :return: the list with the appended thing
    """

    to.append(element)
    return to

extra_credit = 0

# DO NOT CHANGE ANYTHING BELOW THIS LINE
# Test section. All these tests should pass when run as follows.
#
# After you have solved the initial problem,
# if you want to go for extra credit,
# please to set the extra_credit to 1, or 2
# Then read the tests to see what is expected.

import mock, unittest
class TestAppendTo(unittest.TestCase):

    def setUp(self):
        self._input_list = [mock.sentinel.first, mock.sentinel.second, mock.sentinel.third]

    @property
    def input_list(self):
        return list(self._input_list)

    def test_returns_an_array(self):
        'The method should return a list'
        r = append_to(mock.sentinel.test_returns_an_array, self.input_list)
        self.assertIsInstance(r, list)

    def test_returns_same_array_it_was_given(self):
        'The method should modify the input_list in place'
        input_list_copy = self.input_list
        r = append_to(mock.sentinel.junk, input_list_copy)
        self.assertIs(r, input_list_copy)

    def test_returns_same_empty_array_it_was_given(self):
        'The method should modify the input_list in place'
        input_list = []
        r = append_to(mock.sentinel.junk, input_list)
        self.assertIs(r, input_list)

    def test_append_value_is_last_entry(self):
        'The value passed should be added to the end of the list.'
        v = mock.sentinel.should_be_last_entry
        r = append_to(v, self.input_list)
        self.assertIs(r[-1], v)

    def test_appending_value_to_default_generates_new_list(self):
        'Distinct calls should not have any side-effects.'
        r1 = append_to(mock.sentinel.first_run)
        r2 = append_to(mock.sentinel.second_run)
        self.assertListEqual(r1, [mock.sentinel.first_run])
        self.assertListEqual(r2, [mock.sentinel.second_run])

    @unittest.skipIf(extra_credit < 1, 'Not trying for 1st tier of extra credit')
    def test_scalarization_of_list(self):
        'If thing is not a scalar, flatten it into a scalar'
        v = [mock.sentinel.a, mock.sentinel.b]
        r = append_to(v, self.input_list)
        self.assertListEqual(r, [mock.sentinel.first, mock.sentinel.second, mock.sentinel.third,
                                 mock.sentinel.a, mock.sentinel.b])

    @unittest.skipIf(extra_credit < 2, 'Not trying for 2nd tier of extra credit')
    def test_scalarization_of_dict(self):
        'If thing is not a scalar, flatten it into a scalar'
        v = {mock.sentinel.a: mock.sentinel.b}
        r = append_to(v, self.input_list)
        self.assertListEqual(r, [mock.sentinel.first, mock.sentinel.second, mock.sentinel.third,
                                 mock.sentinel.a])


unittest.main(exit=False)
