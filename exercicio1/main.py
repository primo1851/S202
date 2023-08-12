from Aluno import Aluno
from Aula import Aula
from Professor import Professor


professor = Professor("Lucas")
aluno1 = Aluno("Maria")
aluno2 = Aluno("Pedro")
aula = Aula(professor, "Programação Orientada a Objetos")
aula.adicionar_aluno(aluno1)
aula.adicionar_aluno(aluno2)
print(aula.listar_presenca())

# Presença na aula sobre Programação Orientada a Objetos, ministrada pelo professor Lucas:
# O aluno Maria está presente.
# O aluno Pedro está presente.