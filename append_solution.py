
# Note, None instead of a literal []
def append_to(element, to=None):
    if to is None:      # test if None
        to = []
    to.append(element)
    return to

"""
Expect an explanation around compile time instantiation vs runtime.
"""
