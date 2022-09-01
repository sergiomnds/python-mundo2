
#? Trabalhando com condições aninhadas. else if dentro de um if else.
#? Em Python else if -> elif
nome = str(input('Qual é o seu nome? '))

if nome == 'Serjo':
    print('Nome bonito!')
elif nome in 'Gabriel Sergio Serjao':
        print('Esse nome aí...')
else:
    print('Seu nome é OK.') 
    
print('Tenha um bom dia, {}!'.format(nome))
