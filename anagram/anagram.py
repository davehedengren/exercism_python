def detect_anagrams(word,a_list):
    anagrams = []
    for a in a_list:
        if ((sorted(word.lower())) == sorted(a.lower()) 
            and word.lower() != a.lower()):
            anagrams.append(a)
    return anagrams
