n1 = float(input('Digite sua altura, em metros: '))
n2 = float(input('Digite seu peso, em quilos: '))
n3 = n2 / (n1 ** 2)
if n3 < 18.5:
    print('Seu IMC é {:.2f}. Você está abaixo do peso.'.format(n3))
elif 18.5 <= n3 < 25:
    print('Seu IMC é {:.2f}. Você está no peso ideal.'.format(n3))
elif 25 <= n3 < 30:
    print('Seu IMC é {:.2f}. Você está com sobrepeso.'.format(n3))
elif 30 <= n3 < 40:
    print('Seu IMC é {:.2f}. Você está com obesidade.'.format(n3))
elif n3 >= 40:
    print('Seu IMC é {:.2f}. Você está com obesidade mórbida'.format(n3))
