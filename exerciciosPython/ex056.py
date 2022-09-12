
# ?  Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# ?  No final do programa, mostre: a média de idade do grupo,
# ?  qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
idadeVelho = 0
nomeVelho = ''
idadeTodos = 0
mulheresMenos20 = 0

for c in range(1, 5):
    nome = str(input(f"Digite o nome da {c}ª pessoa: ")).strip()

    idade = int(input('Digite a idade dessa pessoa: '))
    idadeTodos += idade

    sexo = str(input('Digite o sexo dessa pessoa (M ou F): ')).strip().upper()

    if c == 1 and sexo in 'M':
        nomeVelho = nome
        idadeVelho = idade

    if sexo in 'M' and idade > idadeVelho:
        nomeVelho = nome
        idadeVelho = idade

    if sexo in 'F' and idade < 20:
        mulheresMenos20 += 1
mediaIdade = idadeTodos / 4
print(f"A média de idade do grupo é {mediaIdade} anos.")
print(f"O homem mais velho do grupo é o {nomeVelho} com {idadeVelho} anos.")
print(f"O número de mulheres com menos de 20 anos é {mulheresMenos20}.")
