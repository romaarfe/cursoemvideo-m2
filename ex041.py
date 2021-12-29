from datetime import date
n1 = int(input('Digite o seu ano de nascimento: '))
n2 = (date.today().year - n1)
if n2 <= 9:
    print('Atleta de Categoria Mirim!')
elif n2 <= 14:
    print('Atleta de Categoria Infantil!')
elif n2 <= 19:
    print('Atleta de Categoria Júnior!')
elif n2 <= 25:
    print('Atleta de Categoria Sênior!')
else:
    print('Atleta de Categoria Master!')
