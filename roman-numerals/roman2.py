r_num0 = {
         1: 'I',                                                                 
         2: 'II',                                                                
         3: 'III',                                                               
         4: 'IV',                                                                
         5: 'V',                                                                 
         6: 'VI',                                                                
         7: 'VII',                                                                
         8: 'VIII',                                                                
         9: 'IX',
         0: ''
         }
r_num10 = {
        1: 'X',
        2: 'XX',
        3: 'XXX',
        4: 'XL',
        5: 'L',
        6: 'LX',
        7: 'LXX',
        8: 'LXXX',
        9: 'XC',
        0: ''
        }
r_num100 = {
        1: 'C',
        2: 'CC',
        3: 'CCC',
        4: 'CD',
        5: 'D',
        6: 'DC',
        7: 'DCC',
        8: 'DCCC',
        9: 'CM',
        0: ''
    }
r_num1000 = {
    1: 'M',
    2: 'MM',
    3: 'MMM'
    }

def numeral(arabic):
    r_char = ''
    #read from right to left
    a = str(arabic)
    for x in range(len(a)-1,-1,-1):
        if x == len(a)-4:
            r_char = r_num1000[int(a[x])] + r_char
        elif x == len(a)-3:
            r_char = r_num100[int(a[x])] + r_char
        elif x == len(a)-2:
            r_char = r_num10[int(a[x])] + r_char
        elif x == len(a)-1:
            r_char = r_num0[int(a[x])] + r_char
    return r_char
# I bet I could do this in a more concise way by counting distance from 5...
