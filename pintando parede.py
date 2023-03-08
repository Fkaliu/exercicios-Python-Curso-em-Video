# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
n1 = float(input('Informe a largura da parede:'))
n2 = float(input('Informe altura da parede:'))
area = n1*n2
print('Sua parede tem a dimensão de {} x {} e sua área é de {}m²'.format(n1, n2, area))
tin = area / 2
print('para pintar essa parede serão necessarios {} litros de tinta para garantir o serviço'.format(tin))
