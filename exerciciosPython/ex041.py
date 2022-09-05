
#? A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento 
#? de um atleta e mostre sua categoria, de acordo com a idade:
#? – Até 9 anos: MIRIM
#? – Até 14 anos: INFANTIL
#? – Até 19 anos: JÚNIOR
#? – Até 25 anos: SÊNIOR
#? – Acima de 25 anos: MASTER

anoNascimento = int(input("Digite o ano de nascimento: "))
anoAtual = int(2022)
idade = anoAtual - anoNascimento

if idade <= 9:
    print("Idade: {}. Categoria: MIRIM".format(idade))
elif idade <= 14:
    print("Idade: {}. Categoria: INFANTIL".format(idade))
elif idade <= 19:
    print("Idade: {}. Categoria: JÚNIOR".format(idade))
elif idade <= 25:
    print("Idade: {}. Categoria: SÊNIOR".format(idade))
else:
    print("Idade: {}. Categoria: MASTER".format(idade))
