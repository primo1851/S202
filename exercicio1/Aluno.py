class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.presente = False
    def presensa(self):
        print ("O aluno {self.nome} está presente.")
