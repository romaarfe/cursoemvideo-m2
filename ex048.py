print('Vou calcular para você a soma de todos os números ímpares,  entre 1 e 500, que são múltiplos de três:')
result = 0
count = 0
for c in range(1, 500, 2):
    if (c % 3) == 0:
        result += c  # Igual result = result + c
        count += 1  # Igual count = count + 1
print('A soma de todos os {} valores solicitados é {}.'.format(count, result))
