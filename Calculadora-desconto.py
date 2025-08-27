print ('------Calculadora de descontos------')

preco = float(input('Qual o preço do produto?: '))
desconto = float(input('Qual o desconto do produto?: '))

valor_do_desconto = (preco * desconto) / 100
preco_final = preco - valor_do_desconto

print(f'O valor do desconto é de R${valor_do_desconto}')
print(f'O preço final do produto é de R${preco_final}')
