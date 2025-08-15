peso = float(input('Digite o seu peso em kg: '))
altura = float(input('digite a sua altura em metros: '))

imc = peso / (altura * altura)

print(f'Seu IMC é {imc:.2f}')

