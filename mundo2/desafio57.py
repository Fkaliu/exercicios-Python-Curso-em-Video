#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.
op1 = ''
nome = str(input('Digite o seu nome: ')).strip().upper()
sexo = str(input('Informe o seu sexo: [M/F] ')).strip().upper()
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Dados invalidos, Por favor, informe seu sexo: ')).strip().upper()
if sexo == 'M':
    op1 = 'Bora tomar uma?'
else:
    op1 = 'Bora fumar um?'
print('Olá {}. Tenha um bom dia'.format(nome))
print(op1)
#print(sexo)
