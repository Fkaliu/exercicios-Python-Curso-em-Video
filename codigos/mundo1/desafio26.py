#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input('Digite uma frase: ')).upper().strip() #aprendi essa hoje
print('A letra {} aparece vezes na frase.'.format(frase.count('A')))
print('A primeira letra apareceu na posição {}.'.format(frase.find('A')+1)) #aprendi essa hoje
print('A ultima letra apareceu na posição {}'.format(frase.rfind('A')+1)) #aprendi essa hoje

