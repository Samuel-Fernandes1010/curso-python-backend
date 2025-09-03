def somar(v1, v2):
  return v1 + v2

def subtrair(v1, v2):
  return v1 - v2  

def multiplicar(v1, v2):
  return v1 * v2

def dividir(v1, v2):
  if v2 == 0:
    print('Não existe divisão por 0.')
    return None
  else:
    return v1 / v2

def menu():
  print('Operações disponíveis:')
  print('1 para somar')
  print('2 para subtrair')
  print('3 para multiplicar')
  print('4 para dividir')
  
def obter_numeros():
    num1 = int(input('Qual o seu 1º número? '))
    num2 = int(input('Qual o seu 2º número? '))
    
    return num1, num2

def main():
  menu()
  op = input('Qual operação você precisa? ')
  num1, num2 = obter_numeros()
  match op:
    case '1':
      r = somar(num1, num2)
      print(f'O resultado é {r}')
      
    case '2':
      r = subtrair(num1, num2)
      print(f'O resultado é {r}')
      
    case '3':
      r = multiplicar(num1, num2)
      print(f'O resultado é {r}')
    case '4':
      r = dividir(num1, num2)
      print(f'O resultado é {r}')
main()

  