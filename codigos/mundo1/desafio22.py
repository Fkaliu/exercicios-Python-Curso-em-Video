#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas e minúsculas / Quantas letras tem no total (sem considerar espaços).
# Quantas letras tem o primeiro nome.
nome = str(input('Digite o seu nome completo: ')).strip()
letras = (len(nome) - nome.count(' '))
primeironome = nome.split()
letraprimeironome = len(primeironome[0])
#print(nome.split())
#print(primeironome[0])
print('Analisando o seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(letras))
print('Seu primeiro nome é {} e ele tem {} letras'.format((primeironome[0]), letraprimeironome))
print('A primeira letra do seu nome é {}'.format((primeironome[0][0])))
