print('Sexo Masculino ou Feminino M/F? ')
sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Qual é o sexo da pessoa: ')).strip().upper()[0]
print('Sexo registrado {}'.format(sexo))

# Professor
sex = str(input('Informe seu sexo: ')).strip().upper()[0]
while sex not in 'MF':
    sex = str(input('Dados invalidos. Informe novamente: ')).strip().upper()[0]
print('Sexo registrado {}'.format(sex))