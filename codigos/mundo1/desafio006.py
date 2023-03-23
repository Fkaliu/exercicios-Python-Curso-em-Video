#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n = int(input('Digite um número '))
d = n*2
t = n*3
r = n**(1/2)

print('O número digitado é "{}", o dobro deste número é "{}"'.format(n, d), end=' ')
print('o triplo deste número é "{}" e a raiz quadrada é "{:.3f}"!'.format(t, r))
