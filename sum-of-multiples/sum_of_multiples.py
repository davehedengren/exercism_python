def sum_of_multiples(x, multiples=[3,5]):
    return sum(set(y for y in range(x) for m in multiples if m > 0 and y
                           % m == 0))
