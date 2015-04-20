
def slices(s,n):
    # Stole Error message from cjchallis
    if len(s) < n or n <= 0:
        raise ValueError("Impossible to find series of length %d in sequence "\
                         "of length %d" %(n, len(s)))
    # had a loop, consolidated to one line thanks to cjchallis
    return [list(map(int, s[start:start+n])) for start in range(len(s)-n+1)]

