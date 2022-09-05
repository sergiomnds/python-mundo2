
#? Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
#? se é a hora exata de se alistar ou se já passou do tempo do alistamento.
#? Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

anoNascimento = int(input('Digite o ano de nascimento: '))
anoAtual = int(2022)
idade = anoAtual - anoNascimento
if idade < 18:
    print('Você tem {} anos. Ainda não precisa se alistar, falta {} ano(s)!'.format(idade, 18 - idade))
    print('Seu alistamento será em {}'.format(anoAtual + (18 - idade)))
elif idade > 18:
    print('Você tem {} anos. Já deveria ter se alistado, passou {} ano(s)!'.format(idade, idade - 18))
    print('Seu alistamento foi em {}'.format(anoAtual - (idade - 18)))
else:
    print('Você tem 18 anos, precisa se alistar esse ano!')
    