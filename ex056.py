count_age = 0
rate_age = 0
high_age_man = 0
high_age_name = ''
women_less20 = 0
for c in range(1, 5):
    print('»»» {}ª PESSOA «««'.format(c))
    name = str(input('Nome: ')).strip()
    age = int(input('Idade: '))
    gender = str(input('Sexo [M/F]: ')).strip()
    count_age += age
    if c == 1 and gender in 'Mm':
        high_age_man = age
        high_age_name = name
    elif gender in 'Mm' and age > high_age_man:
        high_age_man = age
        high_age_name = name
    elif gender in 'Ff' and age < 20:
        women_less20 += 1
rate_age = count_age / 4
print('A média de idade do grupo é de {} anos.'.format(rate_age))
print('O homem mais velho tem {} anos e se chama {}.'.format(high_age_man, high_age_name))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(women_less20))
