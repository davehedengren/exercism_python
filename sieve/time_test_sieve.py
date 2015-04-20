import time

def sieve_cc(N):
    is_prime = [True] * (N+1)
    is_prime[0:2] = [False, False]
    for i in range(0, int(N**0.5+1)):
        if is_prime[i]:
            for j in range(i*i, N+1, i):
                is_prime[j] = False 
    return [i for i in range(0, N+1) if is_prime[i]]

def sieve_am(N):
    sieve = [True for i in range(N+1)]
    primes = []
    stopFactor = int(N**0.5) + 1
    for i in range(2, stopFactor):
        if sieve[i]:
            for j in range(i*i, N, i):
                sieve[j] = False
                primes.append(i) # slightly faster than full range comprehension
    return primes + [i for i in range(stopFactor, N+1) if sieve[i]]

def sieve_dh(n):
    plist = list(range(2,n+1))
    #stopFactor stolen from Alex and Chris
    for y in range(2, int(n**0.5) + 1):
        for x in plist:
            if x % y == 0 and y < x:
                plist.remove(x)
    return plist

am_times = []
for x in range(2,5):
    start_time = time.time()
    sieve_am(10**x)
    end_time = time.time()-start_time
    am_times.append(end_time)

cc_times = []
for x in range(2,5):
    start_time = time.time()
    sieve_cc(10**x)
    end_time = time.time()-start_time
    cc_times.append(end_time)

dh_times = []
for x in range(2,5):
    start_time = time.time()
    sieve_dh(10**x)
    end_time = time.time()-start_time
    dh_times.append(end_time)

print("AM", am_times)
print("CC", cc_times)
print("DH", dh_times)
