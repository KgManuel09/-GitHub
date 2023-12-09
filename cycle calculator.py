import math as mh

f_a = float(input('var f_a'))

f_b = float(input('var f_b'))

f_c = float(input('var f_c'))

i_d = int(input('var i_d'))

act = input('act')

if act == '+':
    print(f_a + f_b)
elif act == '-':
    print(f_a - f_b)
elif act == '*':
    print(f_a * f_b)
elif act == '/':
    print(f_a / f_b)
elif act == '**':
    print(f_a ** f_b)
elif act == '%':
    print(f_a % f_b)
elif act == '//':
    print(f_a // f_b)
elif act == 'abs':
    print(abs(f_c))
elif act == 'sqrt':
    print(mh.sqrt(f_c))
elif act == 'log':
    print(mh.log(f_c))
elif act == 'sin':
    print(mh.sin(f_c))
elif act == 'cos':
    print(mh.cos(f_c))
elif act == 'tan':
    print(mh.tan(f_c))
elif act == '!':
    print(mh.factorial(i_d))
elif act == 'rd':
    print(round(f_c, i_d))
elif act == 'cbrt':
    print(mh.cbrt(f_c))
else:
    print(f'error: act {act} not found')
