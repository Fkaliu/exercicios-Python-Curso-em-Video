#Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
print('{} Os Termos de uma PA {}'.format('>'*10, '<'*10))
n = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = n + (10-1) * razao
termo = n
c = 1
while c <= 10:
    print('{} '.format(termo), end='')
    termo += razao
    c += 1
print('>> o decimo termo é: ', decimo)


