#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento: (à vista dinheiro/cheque: 10% de desconto | à vista no cartão: 5% de desconto | em até 2x no cartão: preço formal | 3x ou mais no cartão: 20% de juros)
print('{:=^30}'.format('LOJAS KALIU'))
preco = float(input('Digite o valor do produto: '))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/PIX (10% de DESCONTO)')
print('[ 2 ] à vista cartão (5% de DESCONTO)')
print('[ 3 ] 2x no cartão (sem juros)')
print('[ 4 ] 3x ou mais no cartão (com juros)')
opcao = int(input('Qual e a opção de pagamento? '))
if opcao == 1:
    des10 = preco - (preco * 10 / 100)
    print('O valor do produto com um desconto de 10% sera de R${:.2f}!'.format(des10))
elif opcao == 2:
    des5 = preco - (preco * 5 / 100)
    print('o valor do produto a vista no cartão, com um desconto de 5% será de R${:.2f}'.format(des5))
elif opcao == 3:
    divide = preco / 2
    print(' o valor divido em 2x no cartão, sem desconto será de R${:.2f}'.format(divide))
elif opcao == 4:
    opcao2 = int(input('Quantas parcelas? '))
    if opcao2 <= 2:
        print('OPÇÃO INVALIDA')
    else:
        parcelas = preco / opcao2
        juros = parcelas + (parcelas * 20 / 100)
        total = juros * opcao2
        print('Sua compra será parcelada em {}x de R${:.2f} com JUROS'.format(opcao2, juros))
        print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco, total))
else:
    print('OPÇÃO INVALIDA')
