import random

num_secreto = random.randint(0, 100)
palpite = 0
print ('----Jogo de advinhação----')
print ('Tente advinhar um número de 0 a 100.')
while palpite != num_secreto:
    palpite_str = input ('Qual o seu palpite? ')
    if palpite_str.isdigit():
        palpite = int(palpite_str)
        if palpite > 100:
            print ('Número fora de escala, tente outro valor. ')
        elif palpite > num_secreto:
            print ('N° muito alto, tente novamente.')
        elif palpite < num_secreto:
            print ('N° muito baixo, tente novamente. ')
    else:
        print ('Valor inválido, digite outro número, ')
print(f'Parabéns você acertou o número {num_secreto}')