#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome = str(input('Digite o seu nome completo: ')).upper().strip()
separado = nome.split()
print(separado)
print('Seu primeiro nome é {}'.format(separado[0]))
print('Seu ultimo nome é {}'.format(separado[-1]))#boa

