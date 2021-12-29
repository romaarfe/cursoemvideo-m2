n = int(input('Digite o número inteiro que será convertido: '))
option = int(input('Agora escolha uma opção: [1] para Binário, [2] para Octal ou [3] para Hexadecimal: '))
if option == 1:
    print('{} convertido para Binário é {}.'.format(n, format(n, 'b')))
elif option == 2:
    print('{} convertido para Octal é {}.'.format(n, format(n, 'o')))
elif option == 3:
    print('{} convertido para Hexadecimal é {}.'.format(n, format(n, 'x')))
else:
    print('Esta opção não é válida. Tente novamente!')
