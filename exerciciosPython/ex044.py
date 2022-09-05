
#? Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#? – à vista dinheiro/cheque: 10% de desconto
#? – à vista no cartão: 5% de desconto
#? – em até 2x no cartão: preço formal 
#? – 3x ou mais no cartão: 20% de juros

preco = float(input("Digite o preço do produto: "))
print('''Escolha a forma de pagamento:
      1 - À vista dinheiro/cheque
      2 - À vista no cartão
      3 - Em até 2x no cartão
      4 - 3x ou mais no cartão''')
escolha = int(input("Digite a opção: "))

if escolha == 1:
    preco = preco * 0.9
    print("O preço final do produto é R${:.2f}".format(preco))
elif escolha == 2:
    preco = preco * 0.95
    print("O preço final do produto é R${:.2f}".format(preco))
elif escolha == 3:
    print("O preço final do produto é R${:.2f}".format(preco))
    print("O produto será parcelado em 2x de R${:.2f}".format(preco / 2))
elif escolha == 4:
    preco = preco * 1.2
    parcelas = int(input("Digite o número de parcelas: "))
    print('O preço final do produto é R${:.2f}'.format(preco))
    print('O produto será parcelado em {}x de R${:.2f}'.format(parcelas, (preco / parcelas)))
else:
    print('Opção inválida!')
