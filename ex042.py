print('Analisador de triângulos...')
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima PODEM formar um triângulo!')
    if a == b == c:
        print('E esse triângulo é Equilátero.')
    elif a == b or b == c or a == c:
        print('E esse triângulo é Isósceles.')
    else:
        print('E esse triângulo é Escaleno.')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo!')
