soma = maior = menor = cont = 0
barato = ''
while True:
    produto = str(input('Qual o nome do produto? '))
    valor = float(input('Qual o valor do produto? R$ '))
    cont += 1
    soma += valor
    if valor >= 1000:
        maior += 1
    if cont == 1 or valor < menor:
        menor = valor
        barato = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'O total gasto foi de R$ {soma}.')
print(f'E tem {maior} produtos mais caros que R$ 1000.')
print(f'O produto mais barato é {barato} e ele custa {menor}.')
