n1 = str(input('Digite um possível palíndromo: ')).strip().upper()
n2 = n1.split()
n3 = ''.join(n2)
n4 = ''
for c in range(len(n3) - 1, - 1, - 1):
    n4 += n3[c]
print('O inverso de {} é {}.'.format(n3, n4))
if n4 == n3:
    print('Temos um palíndromo!')
else:
    print('Não é um palíndromo!')
