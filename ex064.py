n = 0
n1 = 0
n2 = -1
while n != 999:
    n = int(input('Digite um número inteiro [999 para PARAR]: '))
    if n != 999:
        n1 += n
    n2 += 1
print('Você saiu do programa. E digitou {} números, sendo seu somátorio igual a {}.'.format(n2, n1))
