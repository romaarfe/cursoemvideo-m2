from time import sleep
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
n3 = 1
maior = 1
while n3 != 5:
    n3 = int(input('''Escolha uma das opções abaixo:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair do Programa
Qual a sua escolha? '''))
    print('#'*40)
    if n3 == 1:
        print('{} + {} = {}'.format(n1, n2, n1 + n2))
    elif n3 == 2:
        print('{} x {} = {}'.format(n1, n2, n1 * n2))
    elif n3 == 3:
        if n2 > n1:
            print('O número maior é {}.'.format(n2))
        else:
            print('O número maior é {}.'.format(n1))
    elif n3 == 4:
        n1 = int(input('Digite um novo número inteiro: '))
        n2 = int(input('Digite outro novo número inteiro: '))
    else:
        print('Opção inválida. Escolha outra opção!')
    print('#'*40)
    sleep(2)
print('Você saiu do Programa.')
