n = c = 1
while True:
    n = int(input('Digite um número para saber sua tabuada: '))
    if n <= 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c:2} = {n * c}')
print('Você encerrou sua tabuada.')
