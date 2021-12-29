mf = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
while mf not in 'MmFf':
    mf = str(input('Você digitou uma opção errada, por favor tente novamente: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(mf))
