# Classe base (pai)
class MembroUEPA:
    def __init__(self, nome, matricula, email):
        self.nome = nome
        self.matricula = matricula
        self.email = email

    def apresentar(self):
        return f"Olá, eu sou um membro da UEPA. Nome: {self.nome}"


# Classe filha Aluno → Herança de MembroUEPA
class Aluno(MembroUEPA):
    def __init__(self, nome, matricula, email, curso):
        # super() chama o construtor da classe pai para inicializar nome, matricula e email
        super().__init__(nome, matricula, email)
        self.curso = curso

    def verificar_notas(self, notas):
        media = sum(notas) / len(notas)
        if media >= 7:
            return f"O aluno {self.nome} foi aprovado com média {media:.1f}."
        else:
            return f"O aluno {self.nome} foi reprovado com média {media:.1f}."

    # Sobrescrita do método apresentar()
    def apresentar(self):
        return f"Sou o aluno {self.nome}, do curso de {self.curso}."


# Classe filha Professor → Herança de MembroUEPA
class Professor(MembroUEPA):
    def __init__(self, nome, matricula, email, departamento):
        super().__init__(nome, matricula, email)
        self.departamento = departamento

    def lancar_frequencia(self, presencas):
        return f"Frequência lançada: {presencas} alunos presentes."

    # Sobrescrita do método apresentar()
    def apresentar(self):
        return f"Sou o professor {self.nome}, do departamento de {self.departamento}."


#Testes

if __name__ == "__main__":
    # Criando um aluno
    aluno1 = Aluno("Maria", "2023001", "maria@uepa.br", "Engenharia")
    print(aluno1.apresentar())
    print(aluno1.verificar_notas([8.0, 6.5, 7.5]))

    # Criando um professor
    prof1 = Professor("Carlos", "P12345", "carlos@uepa.br", "Computação")
    print(prof1.apresentar())
    print(prof1.lancar_frequencia(25))
