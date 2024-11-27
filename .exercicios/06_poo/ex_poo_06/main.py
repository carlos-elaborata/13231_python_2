from alunos import Aluno

aluno_1 = Aluno(nome="João", idade=20)

try:
    print(aluno_1.adicionar_disciplina(disciplina="Matemática"))
except ValueError as e:
    print(e)
try:
    print(aluno_1.adicionar_disciplina(disciplina="Matemática"))
except ValueError as e:
    print(e)
try:
    print(aluno_1.adicionar_disciplina(disciplina="Física"))
except ValueError as e:
    print(e)

try:
    print(aluno_1.remover_disciplina(disciplina="Matemática"))
except ValueError as e:
    print(e)
try:
    print(aluno_1.remover_disciplina(disciplina="História"))
except ValueError as e:
    print(e)

print(aluno_1.verificar_disciplina(disciplina="Geografia"))
print(aluno_1.verificar_disciplina(disciplina="Física"))
