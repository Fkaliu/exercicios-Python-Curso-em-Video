#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
print('O valor da diária do carro é de: R$ 60 por dia e cobramos um preço de R$0,15 por Km rodado')
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Kms rodados? '))
precokm = km * 0.15
preco = (dias * 60)
cobrar = preco + precokm
desconto = cobrar - (cobrar * 10 / 100)
print('O valor a pagar pelo aluguel do carro é de R${:.2f}!'.format(cobrar))
print('Vai ser no dinheiro ou cartão? Caso opte por cartão/pix vc ganha um desconto de 10 %')
print('O preço do aluguel com o desconto aplicado é de R${}!'.format(desconto))


