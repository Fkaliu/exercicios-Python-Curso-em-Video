#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
n = float(input('Digite uma distancia em metros: '))
print('A medida de {} corresponde a '.format(n))
print('{}km'.format(n/1000))
print('{}cm'.format(int(n*100)))
print('{}mm'.format(int(n*1000)))






