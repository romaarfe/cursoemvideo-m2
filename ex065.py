resp = 'S'
soma = quant = media = maior = menor = 0
while resp == 'S':
    num = int(input('Digite um número inteiro: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    resp = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
media = soma / quant
print('Você digitou {} números e a média foi {}.'.format(quant, media))
print('O maior valor foi {} e menor foi {}.'.format(maior, menor))
