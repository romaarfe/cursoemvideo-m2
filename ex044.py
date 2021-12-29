n1 = float(input('Digite o valor do produto: R$ '))
n2 = int(input('Informe a condição de pagamento: 1 para Dinheiro/Cheque ou 2 para Cartão: '))
n3 = int(input('O pagamento será à vista ou à prazo? 1 para À Vista ou 2 para à Prazo: '))
if n2 == 1 and n3 == 1:
    print('Você recebeu 10% de desconto. O novo valor é de R${:.2f}'.format(n1-(n1*10/100)))
elif n2 == 2 and n3 == 1:
    print('Você recebeu 5% de desconto. O novo valor é de R${:.2f}'.format(n1-(n1*5/100)))
elif n2 == 2 and n3 == 2:
    n4 = int(input('Digite em quantas vezes deseja pagar: '))
    if n4 <= 3:
        print('Você manteve o valor normal de R${:.2f}. E pagará R${:.3f} em {} vezes.'.format(n1, (n1/n4), n4))
    elif n4 > 3:
        print('Você pagará com 20% de juros. Serão R${:.3f} em {} vezes.'.format((n1+(n1*20/100))/n4, n4))
else:
    print('Esta opção não á válida!')
