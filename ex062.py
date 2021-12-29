primeiro = int(input('Digite o Primeiro Termo da PA: '))
razão = int(input('Digite a Razão da PA: '))
termo = primeiro
cont = 1
total = 0
extras = 10
while extras != 0:
    total = total + extras
    while cont <= total:
        print('{} » '.format(termo), end='')
        cont += 1
        termo = termo + razão
    print('PAUSA!')
    extras = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
