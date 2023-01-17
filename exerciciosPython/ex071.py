
#? Simule o funcionamento de um caixa eletrônico.
#? No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
#? e o programa vai informar quantas cédulas de cada valor serão entregues.
#? OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

while True:
    cedulasCinquenta = cedulasVinte = cedulasDez = cedulasUm = 0
    print('######CAIXA ELETRÔNICO######')
    valorSacar = int(input('Qual o valor a ser sacado? R$'))

    while valorSacar >= 50: 
        valorSacar -= 50
        cedulasCinquenta += 1

    while valorSacar >= 20:
        valorSacar -= 20
        cedulasVinte += 1

    while valorSacar >= 10:
        valorSacar -= 10
        cedulasDez += 1

    while valorSacar >= 1:
        valorSacar -= 1
        cedulasUm += 1

    print(f'''Foram sacados {cedulasCinquenta} notas de R$50,00
{cedulasVinte} notas de R$20,00
{cedulasDez} notas de R$10,00
{cedulasUm} notas de R$1,00''')
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja realizar outro saque? (S/N) ')).upper()
    if resposta == 'N':
        break
print('Volte Sempre!')