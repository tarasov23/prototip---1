def roman_int(num):
    res = 0
    cif = {'CM':900, 'CD':400, 'XC': 90, 'XL': 40, 'IX': 9, 'IV':4,
        'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    for k in cif:
        res += cif[k] * num.count(k)
        num = num.replace(k, '')
    return res

def int_roman(num):
    num = int(num)
    info = ['I', 'X', 'C', 'M']
    weird_number = ''
    i = 0
    while num != 0:
        n = num % 10
        weird_number = info[i] * n + weird_number
        num //= 10
        i += 1
    res = weird_number
    res = res.replace('IIIIIIIII','IX')
    res = res.replace('IIIII', 'V')
    res = res.replace('IIII', 'IV')
    res = res.replace('XXXXXXXXX','XC')
    res = res.replace('XXXXX','L')
    res = res.replace('XXXX','XL')
    res = res.replace('CCCCCCCCC','CM')
    res = res.replace('CCCCC','D')
    res = res.replace('CCCC','CD')
    return res
    
