n = s = c = 0
while True:
    n = int(input('Digite um número [999 faz PARAR]: '))
    if n == 999:
        break
    s += n
    c += 1
print(f'Você digitou {c} valores e a soma destes números inteiros é {s}.')
