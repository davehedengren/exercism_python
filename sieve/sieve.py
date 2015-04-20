def sieve(n):
    plist = list(range(2,n+1))
    #stopFactor stolen from Alex and Chris
    for y in range(2, int(n**0.5) + 1):
        for x in plist:
            if x % y == 0 and y < x:
                plist.remove(x)
    return plist
