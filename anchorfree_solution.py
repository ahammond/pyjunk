

r = []
# candidates should recognize that start, stop, step map exactly to the range function
for n in range(start, stop, step):
    # doing the modulo once and caching the results is nice
    is_anchor = n % anchor == 0
    is_free = n % free == 0
    if is_anchor and is_free:
        r.append('WOW')
    elif is_anchor:
        r.append('anchor')
    elif is_free:
        r.append('free')
    else:
        r.append(str(n))    # remember to stringify the result
return r
