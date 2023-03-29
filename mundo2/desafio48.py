#Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
soma = 0 #um acumulador?? (ver depois oq é isso)
contador = 0
for n in range(1, 501):
    if n % 2 == 1: #calcular os numeros impares usando o resto da divisão
        if n % 3 == 0: #calcular quais numeros impares são multoplos de 3 usando o resto da divisão
            soma += n #mesma coisa que soma = soma + n
            contador += 1
            #o contador vai contar quantos numeros foram somados 10 total
            print(n)
print('a soma de todos os {} valores é {}'.format(contador, soma))
print('fim')
