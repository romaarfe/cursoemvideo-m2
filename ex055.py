weight_up = 0
weight_down = 0
for c in range(1, 6):
    n = float(input('Peso da {}ª pessoa: '.format(c)))
    if c == 1:
        weight_up = n
        weight_down = n
    else:
        if n > weight_up:
            weight_up = n
        elif n < weight_down:
            weight_down = n
print('O maior peso lido foi de {}Kg.'.format(weight_up))
print('E o menor peso lido foi de {}Kg.'.format(weight_down))
