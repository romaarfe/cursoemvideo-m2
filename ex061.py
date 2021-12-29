primeiro = int(input('Digite o Primeiro Termo da PA: '))
razão = int(input('Digite a Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} » '.format(termo), end='')
    cont += 1
    termo = termo + razão
print('FIM!')
