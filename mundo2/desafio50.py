#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma = 0
cont = 0
for n in range(1, 7):
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        soma = soma + n
        cont = cont + 1
print('vc informou {} numeros pares e a soma dos valores pares é: {}'.format(cont, soma))
print('fim')