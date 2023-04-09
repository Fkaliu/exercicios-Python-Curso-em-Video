#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre: A) qual é o total gasto na compra. B) quantos produtos custam mais de R$1000. C) qual é o nome do produto mais barato.
print('{}'.format('-'*40))
print('{}{}'.format(' '*10,'LOJAS KALIU'))
print('{}'.format('-'*40))
soma = mais1000 = menorpreco =  cont = 0
maisbarato = ' '
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    soma = soma + preco
    cont += 1
    if preco >= 1000:
        mais1000 += 1
    if cont == 1:
        menorpreco = preco
        maisbarato = produto
    else:
        if preco < menorpreco:
            menorpreco = preco
            maisbarato = produto
    escolha = ' '
    print('{}'.format('-'*40))
    while escolha not in 'SN':
        escolha = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break
print('{} FIM DO PROGRAMA {}'.format('-'*12,'-'*12))
print(f'O total da compra foi {soma:.2f}')
print(f'Temos {mais1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {maisbarato} e custa {menorpreco:.2f}')
