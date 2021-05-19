import sqlite3

nome_banco = input('Insira o nome do banco de dados:')

conexao = sqlite3.connect(nome_banco)

cursor = conexao.cursor()

cursor.execute("""
create table controle_notas (
    nome text not null,
    turma integer,
    bimestre integer,
    nota01 float,
    nota02 float,
    nota03 float
);
""")
print('Tabela criada com sucesso')
cursor.close()
conexao.close()
