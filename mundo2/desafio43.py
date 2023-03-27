#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo: (IMC abaixo de 18,5: Abaixo do Peso | Entre 18,5 e 25: Peso Ideal | 25 até 30: Sobrepeso | 30 até 40: Obesidade | Acima de 40: Obesidade Mórbida)
print('Abaixo de 18,5 = ABAIXO DO PESO')
print('Entre 18,5 e 25 = PESO IDEAL')
print('Entre 25 e 30 = SOBREPESO')
print('Entre 30 até 40 = OBESIDADE')
print('Acima de 40 = OBESIDADE MORBIDA')
peso = float(input('Qual o seu peso? (kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC desta pessoa é de: {:.1f}'.format(imc))
if imc < 18.5:
    print('ABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print('Peso ideal')
elif 25 <= imc < 30:
    print('SOBREPESO')
elif 30 <= imc < 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MORBIDA, vai procurar um medico irmão')
