num1 = float(input('Digite o primeiro número: '))
op = input('digite a operação (+, -, *, /): ')
num2 = float(input('Digite o segundo número: '))
print('-----=Resultado------')

match op:
    case '+':
        soma = num1 + num2
        print(soma)
        
    case '-':
        sub = num1 - num2
        print(sub)
    case '*':
        mult = num1 * num2
        print(mult)
    case '/':
        if num2 == 0:
            print('Não dá pra dividir por zero ponba leza')
        else:
            div = num1 / num2
            print(f'{div:.4f}')
    case _:
        print('Operação inválida')
        
        