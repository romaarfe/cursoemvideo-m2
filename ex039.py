from datetime import date
sexo = int(input('Digite [1] para sexo Masculino e [2] para sexo Feminino: '))
if sexo == 1:
    n1 = int(input('Informe o ano do seu nascimento, com quatro dígitos: '))
    n2 = date.today().year - n1
    if n2 < 18:
        print('Você ainda vai ser alistar. Falta(m) {} ano(s).'.format(18 - n2))
    elif n2 == 18:
        print('Você está na época de se alistar.')
    else:
        print('Você já passou do prazo de alistamento em {} ano(s)!'.format(n2 - 18))
elif sexo == 2:
    print('Você não precisa se alistar obrigatoriamente.')
else:
    print('Opção inválida. Por favor, escolha uma opção válida.')
