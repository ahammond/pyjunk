
# Note, None instead of a literal []
def append_to(element, to=None):
    if to is None:      # test if None
        to = []
    to.append(element)
    return to

# Expect an explanation around compile time instantiation vs runtime.

# Next step is to have the candidate work through the UTs and explain how they work.
# Do they understand the concept of mocks?

# Extra credit 1: flatten list and extend
# candidate should describe what the test expects,
# figure out that it requires them to flatten the element by effectively extending the list.

def append_to(element, to=None):
    if to is None:      # test if None
        to = []
    if isinstance(element, list):
        to.extend(element)
    else:
        to.append(element)
    return to


# Extra credit 2: flatten dict and extend

def append_to(element, to=None):
    if to is None:      # test if None
        to = []
    if isinstance(element, (tuple, list)):
        to.extend(element)
    elif isinstance(element, dict):
        to.extend(list(element))
    else:
        to.append(element)
    return to


# General solutions: candidate actually knows python really well.

def append_to(element, to=None):
    if to is None:      # test if None
        to = []
    try:
        for i in element:
            to.append(i)
    except:
        to.append(element)
    return to


# The best solution, because it doesn't require slow, expensive exception handling.

import collections
def append_to(element, to=None):
    if to is None:      # test if None
        to = []
    if isinstance(element, collections.Iterable):
        to.extend(list(element))
    else:
        to.append(element)
    return to
