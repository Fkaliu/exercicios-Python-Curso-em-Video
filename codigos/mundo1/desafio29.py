#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
velocidade = float(input('Qual é a velocidade atual do carro? '))
limite = int(80)
diferença = velocidade - limite
multa = diferença * 7
#print(diferença)
#print(multa)
if velocidade > limite:
    print('VocÊ foi multado pois exedeu o limite de segurança permitido que é de {}km/h'.format(limite))
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
