#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
valorcasa = float(input('Valor da casa: R$'))
salario = float(input('Salario do comprador R$'))
tempo = int(input('Quantos anos de financiamento? '))
prestacao = valorcasa / (tempo * 12)
limite = salario - (salario * 70 / 100)
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}.'.format(valorcasa, tempo, prestacao))
if prestacao > limite:
    print('Empréstimos NEGADO pois o valor da parcela ultrapassa o limite de 30% do salário')
else:
    print('Empréstimo APROVADO! Boa sorte nessa nova jornada!')
#print(valorcasa)
#print(salario)
#print(prestacao)
#print(limite)
