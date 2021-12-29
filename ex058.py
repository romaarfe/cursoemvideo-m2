from random import randint
pc = randint(0, 10)
win = False
guess = 0
print('Estou pensando em um número entre 0 e 10...')
while not win:
    player = int(input('Tente adivinhar que número é esse: '))
    guess += 1
    if player == pc:
        win = True
    else:
        if player < pc:
            print('Mais... Tente mais uma vez: ')
        elif player > pc:
            print('Menos... Tente novamente: ')
print('Parabéns, você acertou! O número que eu pensei foi {}! E você precisou de {} tentativas.'.format(pc, guess))
