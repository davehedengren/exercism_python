def distance(dna1,dna2):
    #Collapsed to one line thanks zip insite from ginebig
    return sum(a != b for a, b in zip(dna1,dna2))
