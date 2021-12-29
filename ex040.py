n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
n3 = (n1+n2)/2
if n3 < 5.0:
    print('Sua média é {:.1f}. Você foi REPROVADO!'.format(n3))
elif n3 >= 7.0:
    print('Sua média é {:.1f}. Você foi APROVADO!!!'.format(n3))
else:
    print('Sua média é {:.1f}. Você está de RECUPERAÇÃO.'.format(n3))
