result = 0
count = 0
for c in range(1, 7):
    n = int(input('Digite o {}º valor: '.format(c)))
    if (n % 2) == 0:
        result += n
        count += 1
print('Você informou {} número(s) par(es) e seu somatório é igual a: {}'.format(count, result))
