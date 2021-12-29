n1 = int(input('Digite o Primeiro Termo da PA: '))
n2 = int(input('Digite a Razão da PA: '))
n3 = n1 + (10 - 1) * n2
for c in range(n1, n3 + n2, n2):
    print(c, end=' » ')
print('ACABOU!')
