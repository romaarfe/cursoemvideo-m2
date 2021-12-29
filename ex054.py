from datetime import date
count_old = 0
count_young = 0
for c in range(1, 8):
    n = int(input('Digite o ano do nascimento da {}º pessoa: '.format(c)))
    if (date.today().year - n) >= 21:
        count_old += 1
    else:
        count_young += 1
print('{} pessoa(s) são maior(es) de idade.'.format(count_old))
print('E {} pessoa(s) ainda é(são) menor(es) de idade.'.format(count_young))
