import random
n = str(input('Vamos jogar Jokenpô? Escolha entre Pedra, Papel ou Tesoura: '))
jokenpo = random.choice(['Pedra', 'Papel', 'Tesoura'])
print('Você escolheu {} e eu escolhi {}.'.format(n, jokenpo))
if n == 'Tesoura' and jokenpo == 'Papel':
    print('Tesoura corta Papel. Você me venceu! Quer jogar novamente?')
elif n == 'Tesoura' and jokenpo == 'Pedra':
    print('Pedra quebra Tesoura. Você perdeu! Vamos jogar de novo?')
elif n == 'Pedra' and jokenpo == 'Papel':
    print('Papel embrulha Pedra. Eu ganhei de você! Quer jogar novamente?')
elif n == 'Pedra' and jokenpo == 'Tesoura':
    print('Pedra esmaga Tesoura. Você me venceu! Vamos jogar de novo?')
elif n == 'Papel' and jokenpo == 'Pedra':
    print('Papel embrulha Pedra. Você me venceu! Vamos jogar de novo?')
elif n == 'Papel' and jokenpo == 'Tesoura':
    print('Tesoura corta Papel. Você perdeu. Quer jogar novamente?')
elif n == jokenpo:
    print('Empate! Vamos jogar outra vez?.')
else:
    print('Opção inválida. Escolha entre Pedra, Papel e Tesoura.')
