def solve(a,b,c):
    D = (b**2 -4*a*c)**(1/2)
    if D == 0 and D>0:
        x1 = (-b-D)/(2*a)
        x2 = (-b+D)/(2*a)
        return f'Here Is "{a}x² + {b}x + {c} = 0" x1 = {x1} & x2 = {x2}'
    else:
        return f'Here Is Not Any Real Factor In "{a}x² + {b}x + {c} = 0"'
a = float(input('Enter Value Of "a" For "ax² + bx + c = 0 , "a" is not equals to "0"\n'))
if a==0:
    print('The Value Of a is "0" It Is Not Quardic Equations')
    raise ZeroDivisionError('We Can`t Divide By 0')
b = float(input('Enter Value Of "b" For "ax² + bx + c = 0"\n'))
c = float(input('Enter Value Of "c" For "ax² + bx + c = 0"\n'))
print(solve(a,b,c))