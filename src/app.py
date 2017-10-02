'''aplicativo base, que pega input de um número de matrícula,
acessa o banco de dados, e retorna a média de alunos no console.
Esse código base serve apenas para demonstrar o processamento
presente no aplicativo em flask caso não seja possível
acessar o app via web.'''

from classes.database import Database
from classes.alunos import Aluno

Database.initialize()

matricula=int(input("Digite o número de matrícula: "))

if (Database.find_one('alunos',{'_id':matricula}) is not None):
    aluno = Aluno.from_mongo(matricula)
    nome = aluno.nome
    media = (aluno.p1+aluno.p2+aluno.p3)/3
    if (media>=5):
        print('O aluno(a) {} foi aprovado(a) com média {:.1f}'.format(nome,media))
    else:
        print('O aluno(a) {} foi reprovado(a) com média {:.1f}'.format(nome,media))

else:
    print('A matrícula não existe!')