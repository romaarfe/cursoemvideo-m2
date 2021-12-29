

print('Olá, seja bem vindo. Você deseja um empréstimo para comprar uma casa?')
casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o seu salário? R$ '))
anos = int(input('Em quantos anos você quer pagar? '))
prestacao = casa / (anos*12)
if prestacao <= (salario*30)/100:
    print('O valor da prestação é R${:.2f}. O empréstimo poderá ser concedido!'.format(prestacao))
else:
    print('A prestação seria de R${:.2f}. Infelizmente seu empréstimo foi negado!'.format(prestacao))
