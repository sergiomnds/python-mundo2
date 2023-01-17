
#? Crie um programa que leia o nome e o preço de vários produtos.
#? O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#? A) qual é o total gasto na compra.
#? B) quantos produtos custam mais de R$1000.
#? C) qual é o nome do produto mais barato.

totalCompra = produtosCaros = contador = 0
nomeBarato = ' '

print('Vamos registrar Produtos!')
while True:
    nomeProduto = str(input('Qual o nome do produto?'))
    precoProduto = float(input('Qual o valor do produto? R$'))
    totalCompra += precoProduto

    if contador == 1:
        produtoBarato = precoProduto
    else:
        if precoProduto < produtoBarato:
            produtoBarato = precoProduto
            nomeBarato = nomeProduto
    if precoProduto > 1000:
        produtosCaros += 1

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja registrar mais um produto? (S/N) ')).upper()
    if resposta == 'N':
        break

print('Boas compras!')
print(f'''O total da compra foi R${totalCompra}
Foram {produtosCaros} por mais de R$1000,00
O produto mais barato se chama {nomeBarato} custando {produtoBarato}''')
