#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
temp = float(input('Informe a temperatura em °C: '))
F = (temp * 1.8) + 32
print('A temperatura de {}°C corresponde a {}°F!'.format(temp, F))
