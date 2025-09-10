#Primeiro precisamos definir as funções.
def menu():
    print('\n-------Cadastro e consulta de alunos-------')
    print('\nOpções disponíveis:')
    print('1 - Cadastrar novo aluno \n2 - Listar aluno cadastrado \n3 - Buscar aluno por matrícula \n4 - Buscar aluno por nome \n5 - Sair')
    return input('\nEscolha uma opção: ')


def cadastrar_aluno(alunos):
    print('\n---Cadastro de novo aluno---')
    nome = input('\nNome do aluno: ')
    
    while True:#Fazendo a validação para garantir que vamos ter só números na matrícula. O while vai obrigar o usuario colocar apenas números.
        try:
            matricula = int(input('\nNúmero de matrícula: ')) #Fazendo a validação para garantir que vamos ter só números na matrícula.
            
            if any(aluno['matricula'] == matricula for aluno in alunos):
                print('Número de matrícula já cadastrado. Tente novamente.')
            else:
                break   
        except ValueError:#Caso tenha letras no número de matrícula vai dar o ValueError.
            print('Erro: Digite apenas números para o número de matrícula.')
        
    curso = input('\nCurso do aluno: ')
    
    aluno = {
        'nome': nome,
        'matricula': matricula,
        'curso': curso
    }
    alunos.append(aluno)
    print('Aluno cadastrado com sucesso!')
   
def listar_aluno(alunos):
    print('\n---Lista de alunos cadastrados---')
    if not alunos:
        print('Nenhum aluno cadastrado.')
    else:
        for aluno in alunos:
            print(f'Nome: {aluno['nome']} | Matrícula: {aluno['matricula']} | Curso: {aluno['curso']}') 

def buscar_aluno_matricula(alunos):
    print('---Buscar aluno por número de matrícula---')
    
    try:
        matricula = int((input('Digite o número de matrícula: ')))
    except ValueError:
        print('Erro: Digite apenas números.')
        return
        
    encontrado = False
    for aluno in alunos:
        if aluno['matricula'] == matricula:
            print(f'\nAluno encontrado: \n\nAluno: {aluno['nome']} | Matrícula: {aluno['matricula']} | Curso: {aluno['curso']}')
            encontrado = True
            break
    if not encontrado:
        print('\nAluno não encontrado.')

def buscar_aluno_nome(alunos): #Adicionei a busca pelo nome, porque é uma funcionalidade interessante e tava fácil de fazer.
    print('---Buscar aluno por nome---')
    nome  = input('Digite o nome do aluno: ')
    encontrado = False
    for aluno in alunos:
        if aluno['nome'] == nome:
            print(f'\nAluno encontrado: \n\nAluno: {aluno['nome']} | Matrícula: {aluno['matricula']} | Curso: {aluno['curso']}')
            encontrado = True
            break
    if not encontrado:
        print('\nAluno não encontrado.')

def main():
    alunos = [] 
    while True:
        opcao = menu()
        
        if opcao == '1':
            cadastrar_aluno(alunos)
            
        elif opcao == '2':
            listar_aluno(alunos)
            
        elif opcao == '3':
            buscar_aluno_matricula(alunos)
            
        elif opcao == '4':
            buscar_aluno_nome(alunos)
            
        elif opcao == '5':
            print('Saindo do programa...')
            break
            
        else:
            print('Opção inválida! Tente novamente.')
            
if __name__ == '__main__':
    main() #Essa parte é nessessária caso o programa seja usado em um código externo como uma biblioteca.

