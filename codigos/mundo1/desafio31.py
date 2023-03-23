#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
distancia = int(input('Qual a distancia da sua viagem? '))
preço = distancia * 0.5
preço1 = distancia * 0.45
print('Você fará uma viagem de {}Km.'.format(distancia))
if distancia >= 200:
    print('E o preço da sua passagem será de R${:.2f}'.format(preço1))
else:
    print('E o preço da sua passagem será de R${:.2f}'.format(preço))
