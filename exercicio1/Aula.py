class Aula():
    def __init__(self,professor, assunto):
        self.professor = professor
        self.assunto = assunto
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)
                
    def listar_presenca(self):
        presenca = print("Presença na aula sobre {self.assunto}, ministrada pelo professor {self.professor.nome}:\n")     
        for aluno in self.alunos:
            status_presenca = "presente" if aluno.presenca_na_aula else "ausente"
            presenca = print("Aluno {aluno.nome}: {status_presenca}\n")
        
        return presenca
