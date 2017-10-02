'''Aplicativo principal em flask.
O aplicativo aqui desenvolvido recebe o input da home page
Com esse input ele calcular a média do aluno e redireciona para uma página com a situação do aluno (aprovado ou reprovado)
Também é possível verificar a lista de alunos cadastrados no bando de dados em ordem alfabética'''

from flask import Flask, render_template, request
from classes.database import Database
from classes.alunos import Aluno
import pymongo

app = Flask(__name__, template_folder='templates')

@app.route('/') #página principal (input de matricula)
def request_method():
    return render_template('pagina_consulta.html')

@app.before_first_request #inicializar o banco de dados após a primeira request
def initialize_database():
    Database.initialize()

@app.route('/consulta', methods=['POST']) #método de cálculo de média dos alunos, acessando o banco de dados e suas notas a partir do número de matrícula
def fazer_consulta():
    if (str(request.form['matricula']).isnumeric()):
        matricula = int(request.form['matricula'])
        if Database.find_one('alunos', {'_id': matricula}) is not None:
            aluno = Aluno.from_mongo(matricula)
            nome = aluno.nome
            calculo=(aluno.p1+aluno.p2+aluno.p3)/3
            media = round(calculo,1)
            if (media >= 5):
                return render_template("aprovado.html", nome=nome,p1=aluno.p1,p2=aluno.p2,p3=aluno.p3,media=media)
            else:
                return render_template("reprovado.html", nome=nome,p1=aluno.p1,p2=aluno.p2,p3=aluno.p3,media=media)

        else:
            return render_template("invalido.html")
    else:
        return render_template("invalido.html")

@app.route('/alunos') #redirecionar para página com todos os alunos cadastrados
def mostrar_alunos():
    alunos = Database.find('alunos',{}).sort([("nome",pymongo.ASCENDING)])
    return render_template("alunos.html",alunos=alunos)

if __name__ == '__main__':
    app.run()
