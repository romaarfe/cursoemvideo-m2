contidade = masc = fem = 0
while True:
    idade = int(input('Digite sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input(' Digite seu sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        contidade += 1
    if sexo == 'M':
        masc += 1
    if sexo == 'F' and idade < 20:
        fem += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Você quer continuar cadastrando novas pessoas [S/N]? ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'A) {contidade} pessoas tem mais de 18 anos;')
print(f'B) {masc} são homens;')
print(f'C) {fem} são mulheres que tem menos de 20 anos.')
