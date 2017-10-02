'''Programa para gerar alunos para o banco de dados
foi utilizado o método pseudo-randômico randrange para fins de simplicidade'''
import random

from classes.alunos import Aluno
from classes.database import Database

Database.initialize()

lista_nomes= ['João','Carlos', 'Rubens', 'Leonardo', 'Caio', 'Pedro',
              'Mateus','Lucas','Rafael','Guilherme','Gustavo','Ana','Beatriz',
              'Carina','Erika','Rafaela','Viviane','Patrícia','Denize','André','Maria',
              'Paula','Paulo','Henrique','Luciana','José','Ninna']  #lista com primeiros nomes

lista_sobrenomes=['Ambrósio','Silva','Fagundes','Pinto','Souza','Hirota',
                  'Yamada','Cunha','Guanabara','Silveira','Azevedo','Guimarães',
                  'Câmara','Freitas','Santos','Spinola','Costa','Oliveira',
                  'Almeida','Rodrigues','Pereira','Dias','Rosa','Cardoso','Nanni'] #lista com sobrenomes

for i in range(0,100): #loop para gerar 100 alunos com nomes e notas aleatórias
    primeiro_nome=random.randrange(0,len(lista_nomes))
    sobrenome=random.randrange(0,len(lista_sobrenomes))
    nome=lista_nomes[primeiro_nome]+' '+lista_sobrenomes[sobrenome]
    p1 = random.randrange(0,11)
    p2 = random.randrange(0, 11)
    p3 = random.randrange(0, 11)
    aluno_gerado=Aluno(nome,p1,p2,p3)
    aluno_gerado.save_to_mongo()
