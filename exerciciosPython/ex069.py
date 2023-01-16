
#? Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
#? o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#? A) quantas pessoas tem mais de 18 anos.
#? B) quantos homens foram cadastrados.
#? C) quantas mulheres tem menos de 20 anos.

qntHomens = qntMulheres = maiorDeIdade = 0
print('Olá, vamos cadastrar alguns dados!')
while True:
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual o sexo dessa pessoa? (M ou F)')).upper()
    idade = int(input('Qual a idade dessa pessoa? '))

    if sexo == 'M':
        qntHomens += 1
    elif sexo == 'F' and idade < 20:
        qntMulheres += 1

    if idade > 18:
        maiorDeIdade += 1

    print('Pessoa Cadastrada!')
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja cadastrar mais um usuário? (S/N) ')).upper()
    if resposta == 'N':
        break
print(f'''No total {maiorDeIdade} pessoas são maiores de idade,
        \nforam cadastrados {qntHomens} homens,
        \ne são {qntMulheres} mulheres com menos de 20 Anos.''')