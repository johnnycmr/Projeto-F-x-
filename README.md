# Projeto F(X)
Projeto realizado para processo seletivo da empresa F(x)

O projeto desenvolvido trata-se de um serviço web que recebe o número de matrícula de um estudante, e retorne suas notas de provas,
média, e se ele foi aprovado ou não na disciplina (considerando média de aprovação de 5 pontos)

Primeiramente foram gerados 100 alunos com nomes e notas aleatórias, e estes salvos no banco de dados em MongoDB.
O algorítimo gerador de alunos, bem como a classe para o banco de dados e para os alunos estão presentes nas pastas "src" e "classes" com nomes gerador_alunos.py, alunos.py e database.py respectivamente.

Após estabelecido o banco de dados, o código para pegar input do número de matrícula, realizar a busca dentro do banco de dados,
e retornar a média do aluno foi realizado. Tal código (ainda sem utilização do flask) encontra-se na pasta "src" com o nome app.py

Por fim, foi implementado o Flask para utilização do serviço na plataforma web, e foram criadas templates de HTML para melhor visualização
do serviço
O aplicativo final possui nome app_flask.py, e todos os formulários HTML estão na pasta "templates".

Obs.: O serviço não foi hospedado, portanto, para executar o aplicativo é necessário rodar tanto o banco de dados
quanto as páginas HTML localmente.
Obs2.: Não foram geradas dumps do banco de dados, portanto é necessário utilizar o algorítmo gerados de alunos para o funcionamento do aplicativo.


