#This the version I made before I learned about the translate function
def encode(text):
    plain = list("abcdefghijklmnopqrstuvwxyz")
    cipher = list("zyxwvutsrqponmlkjihgfedcba")
    text = text.lower().replace(" ","")
    unique = ''.join(set(text))
    for c in unique:
        text = text.replace(c,cipher[plain.index(c)])
    return text
    


def decode(text):
    plain = "abcdefghijklmnopqrstuvwxyz"
    cipher = "zyxwvutsrqponmlkjihgfedcba"

