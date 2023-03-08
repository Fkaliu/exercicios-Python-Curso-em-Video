#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
n1 = float(input('Informe o valor do produto: R$ '))
des = n1 - (n1 * 5 / 100)
print('O valor do produto é: R${:.2f}, com o desconto aplicado fica por: RS{:.2f}'.format(n1, des))

