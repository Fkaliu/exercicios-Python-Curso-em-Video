#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
numpc = randint(0, 10)
cont = 0
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que vc consegue adivinhar qual foi?')
palpite = int(input('Qual é seu palpite? '))
cont += 1
while palpite != numpc:
    if palpite > numpc:
        print('menos, tente outra vez...')
        palpite = int(input('Qual seu palpite? '))
        cont += 1
    elif palpite < numpc:
        print('mais, tente outra vez')
        palpite = int(input('qual seu palpite? '))
        cont += 1
print('vc acertou com {} tentativas. parabens'.format(cont))
if cont == 1:
    print('De primeira, vc é o brabo!')
elif cont == 2:
    print('Muito bom, vc é fera nisso!')
elif cont == 3:
    print('é.. parabens')
elif cont == 4:
    print('vc pode fazer melhor...')
else:
    print('mas vc é muito ruim na adivinhação...')
