'''Classe Aluno criada para instanciar um objeto aluno com atributos nome, matrícula e notas de prova, além de salvá-los e buscá-los na base de dados'''

import random

from classes.database import Database


class Aluno(object): #criando classe Aluno

    def __init__(self,nome,p1,p2,p3,_id=None): #método inicializador
        self.nome=nome
        self.p1=p1
        self.p2=p2
        self.p3=p3
        if _id is None:
            id_gerado = random.randrange(5000000,9000000)
            while (Database.find_one('alunos',{'_id':id_gerado}) is not None): #Certificando que não haverão dois estudantes com mesma matrícula
                id_gerado = random.randrange(5000000, 9000000)
            self._id=id_gerado
        else:
            self._id = _id


    def json(self): #método formatador em json
        return{
            'nome':self.nome,
            'p1':self.p1,
            'p2':self.p2,
            'p3':self.p3,
            '_id': self._id
        }
    def save_to_mongo(self): #método para salvar no banco de dados
        Database.insert(collection='alunos',
                        data=self.json())



    @classmethod
    def from_mongo(cls,_id): #método buscador que retorna objeto da classe Aluno
        dados_aluno = Database.find_one(collection='alunos',query={'_id':_id})
        return cls(nome=dados_aluno['nome'],
                   p1=dados_aluno['p1'],
                   p2=dados_aluno['p2'],
                   p3=dados_aluno['p3'],
                   _id=dados_aluno['_id'])


