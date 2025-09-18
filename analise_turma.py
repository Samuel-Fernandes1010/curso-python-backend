print ('-----Analisador de Desempenho da Turma-----\n')

alunos = [
    {"matricula": "2025A01", "nome": "Ana Silva", "nota_final": 8.5, "frequencia": 80.0, "status_matricula": "ativo"},
    {"matricula": "2025A02", "nome": "Bruno Costa", "nota_final": 6.8, "frequencia": 95.0, "status_matricula": "ativo"},
    {"matricula": "2025A03", "nome": "Carla Dias", "nota_final": 4.5, "frequencia": 70.0, "status_matricula": "ativo"},
    {"matricula": "2025A04", "nome": "Daniel Farias", "nota_final": 9.5, "frequencia": 90.0, "status_matricula": "ativo"},
    {"matricula": "2025A05", "nome": "Elisa Mendes", "nota_final": 7.5, "frequencia": 65.0, "status_matricula": "desligado"},
    {"matricula": "2025A06", "nome": "Fábio Souza", "nota_final": 9.2, "frequencia": 75.0,"status_matricula": "ativo"},
    {"matricula": "2025A07", "nome": "Giovana Lima", "nota_final": 6.0, "frequencia": 100.0, "status_matricula": "ativo"},
    {"matricula": "2025A08", "nome": "Hugo Rocha", "nota_final": 7.0, "frequencia": 74.9, "status_matricula": "ativo"}
]

#1. Filtrar alunos elegíveis:
# Pra isso usei a função filter() junto com uma função lambda e com o operador lógico "and" para filtra os alunos.
elegiveis = filter(lambda aluno: aluno["frequencia"] >= 75.0 and aluno["status_matricula"] == "ativo", alunos)
#Decidi filtrar os inaptos também, a forma que usei é bem parecida com o dos elegíveis só que uso < 75.0 e no lugar do "and" uso o "or" já que tambem ele pode estar com o status de desligado.
inaptos = filter(lambda aluno: aluno["frequencia"] < 75.0 or aluno["status_matricula"] == "desligado", alunos)

#2. Aplicar Bônus:
# Pra isso usei a função map()  junto com o lambda, aqui usei o **aluno pra desmembrar esse dicionário e poder criar um "clone" em que modifico apenas a variável "nota_final".
#E para adicionar os 10% na nota multiplico a nota_final por 1.1 porque assim economiso linhas já que sai o valor de 110% se eu fosse multiplicar por 0,1 que é 10/100 eu receberia apenas o valor dos 10% da nota e teria que somar com a nota fnal depois.
#E para melhorar a sintaxe usei o round(---, 2) para limitar a nota a duas casas decimais e o min(---, 10) pra garantir que a nota não ultrapasse o 10.
bonus = map(lambda aluno: {**aluno, "nota_final": round(min(aluno["nota_final"] * 1.1, 10), 2)}, elegiveis)
#Como decidi mostrar tambem a lista dos alunos elegíveis mais a nota bonus tive que transformar o meu objeto bonus em uma lista, assim eu posso percorrer alista várias vezes, caso o contrário eu só conseguiria percorres o objeto uma vez.
bonus = list(bonus)

#Como disse decidi printar também a lista dos alunos inaptos e do elegíveis, com o for para organizar melhor.  
print('-----Alunos Inaptos-----')
for aluno in inaptos:
    print(f"Aluno: {aluno['nome']} | Nota: {aluno['nota_final']} | Frequência: {aluno['frequencia']} ")

print('\n-----Alunos Elegíveis + Nota Bônus-----')
for aluno in bonus:
    print(f"Aluno: {aluno['nome']} | Nota: {aluno['nota_final']} | Frequencia: {aluno['frequencia']}")
    
#3. Identificar alunos destaque:
# Apenas filtrei a lista bonus com a condição nota_fina >= 9 pra achar os alunos. 
alunos_destaque = filter(lambda aluno: aluno["nota_final"] >= 9, bonus)
print('\n-----Alunos Destaque-----')
#E utilizei o for pra printar apenas as informações que eu queria dos alunos destaque.
for aluno in alunos_destaque:
    print(f"Aluno: {aluno['nome']} | Nota: {aluno['nota_final']} | Frequência: {aluno['frequencia']}")
print('\nAnálise completa\n')