#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Qual é o salário do funcionário? RS'))
aum10 = salario + (salario * 10 / 100)
aum15 = salario + (salario * 15 / 100)
if salario <= 1250:
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, aum15))
else:
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, aum10))
print('10% de aumento: {}'.format(aum10))
print('15% de aumento: {}'.format(aum15))
