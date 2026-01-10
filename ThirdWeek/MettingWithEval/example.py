txt = '(2+3)/0.25-4*2.1'
print(txt, '=', eval(txt)) # Function eval() calculates part in strings which similar to mathematical

equation = input('Enter equation: ')
print(eval(equation))
