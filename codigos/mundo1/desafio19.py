#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random
a1 = input('Primeiro aluno: ')
a2 = input('Segundo Aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)
print('O aluno escolhido foi = {}!'.format(escolhido))
print('Boa sorte!!!')

#print('Lista de Participantes')
#print('1 - Juão')
#print('2 - Luck')
#print('3 - Marco')
#print('4 - Sky')
