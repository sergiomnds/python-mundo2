
#? Faça um programa que leia o sexo de uma pessoa, 
#? mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Digite o seu sexo (M ou F): ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Inválido. \nDigite o seu sexo (M ou F): ')).strip().upper()[0]

if sexo == 'M':
    print('Sexo masculino registrado com sucesso!')
else:
    print('Sexo feminino registrado com sucesso!')
    