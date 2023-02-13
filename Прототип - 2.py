from Operac import *
num = input('Введите число:')
if num[0] in '1234567890':
    print(int_roman(num))
else:
    print(roman_int(num))
