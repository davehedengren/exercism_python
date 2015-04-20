# Stole this from cjchallis and AlexMooney
translate = {
    1:'I', 4:'IV', 5:'V', 9:'IX',
    10:'X', 40:'XL', 50:'L', 90:'XC',
    100:'C', 400:'CD', 500:'D', 900:'CM',
    1000: 'M'
    }

def numeral(arabic):
    r_char = ''
    # read from right to left
    for v in sorted(translate, reverse=True):
        # remove the largest value you can from the arabic value
        # add the roman numeral to the string
        # repeat until number is gone
        while arabic >= v:
            r_char += translate[v]
            arabic -= v
    return r_char
