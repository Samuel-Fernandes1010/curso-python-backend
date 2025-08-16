#Programa para calcular o custo de uma viagem.

#Coletando as variáveis que irei usar nas contas.
print(' ')
print('-----Seja bem-vindo à calculadora de custo de viagem!-----')
print(' ')

distancia = float(input('Qual a distância que será percorrida em Km? = '))
consumo_medio = float(input('Qual o consumo médio do seu veículo em Km/L? (O consumo médio é quanto seu veículo percorre com 1L de combustível) = '))
preco_combustivel = float(input('Qual o preço atual do combustível por litro (em reais)? = '))

#O primeiro parâmetro que vou calcular é o consumo total da viagem que vai ser calculado dividindo a distância que vai ser percorrida na viagem pelo consumo médio do veículo.
consumo_total = (distancia / consumo_medio)

#O segundo parâmetro que vou calcular vai ser a quantidade de combustível que vai ser gasta durante a viagem, para isso basta multiplicar o consumo total da viagem pelo preço do combustível. 
gasto_combustivel = (consumo_total * preco_combustivel)

#Então é só printar as informaçõs necessárias.
print(' ')
print(f'O seu consumo total de combustível será de {consumo_total:.2f}L.')
print(f'Com o combustível no valor de R${preco_combustivel}, você terá um gasto total com combustível de R${gasto_combustivel:.2f}')
print(' ')
print('Espero ter ajudado!')
print('Tenha uma boa vaigem!')
print(' ')
