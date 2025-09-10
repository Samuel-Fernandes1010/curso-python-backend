operacoes = {
    '1': lambda x, y: x + y,
    '2': lambda x, y: x - y,
    '3': lambda x, y: x * y,
    '4': lambda x, y: x / y if y != 0 else 'Não existe divisão por zero'
}

while True:
    print('Qual a sua operação?')
    print('1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão')
    op = input('Opção: ')
    
    if op in operacoes:
        x = float(input('Digite o seu primeiro número: '))
        y = float(input('Digite o seu segundo número: '))
        
        r = operacoes[op](x, y)
        
        print(f'O seu resultado é: {r}')
        
        print(' ')
        