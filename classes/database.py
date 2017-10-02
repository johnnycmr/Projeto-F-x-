'''Classe para o banco de dados em mongodb, com métodos para inserir dados
 e realizar querys'''

import pymongo

class Database(object): #criando classe para banco de dados em mongodb
    URI="mongodb://127.0.0.1:27017"
    DATABASE = None

    @staticmethod
    def initialize(): #método inicializador, seleciona a coleção F(x)
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE=client['F(x)']

    @staticmethod
    def insert(collection,data): #método para inserir dados
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query): #método para realizar querys
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query): #método para realizar querys
        return Database.DATABASE[collection].find_one(query)

    def find_order(collection, query, ordem): #método para realizar querys ordenando os dados
        return Database.DATABASE[collection].find(query).sort(ordem)


