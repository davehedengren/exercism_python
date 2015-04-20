import operator
import functools

def slices(s,n):
    # Stole Error message from cjchallis
    if len(s) < n or n <= 0:
        raise ValueError("Impossible to find series of length %d in sequence "\
                         "of length %d" %(n, len(s)))
    # had a loop, consolidated to one line thanks to cjchallis
    return [list(map(int, s[start:start+n])) for start in range(len(s)-n+1)]

def largest_product(s,n):
    # http://en.wikipedia.org/wiki/Empty_product
    if n == 0 and s == "":
        return 1
    max = float("-inf")
    slice_list = slices(s,n)
    for p in slice_list:
        max_temp = functools.reduce(operator.mul, p, 1)
        if max < max_temp:
            max = max_temp
    return max


