import sqlite3

col_nome = str(input("Digite o nome: "))
col_turma = int(input("Digite a turma: "))
col_bimestre = int(input("Digite o bimestre: "))
col_nota01 = float(input("Digite a nota01: "))
col_nota02 = float(input("Digite a nota02: "))
col_nota03 = float(input("Digite a nota03: "))

conexao = sqlite3.connect('controle_notas.db')
cursor = conexao.cursor()

lista = [(col_nome,col_turma,col_bimestre,col_nota01,col_nota02,col_nota03)]

cursor.executemany("""
insert into controle_notas(nome, turma, bimestre, nota01, nota02, nota03) values(?,?,?,?,?,?)""", lista)

conexao.commit()
cursor.close()
conexao.close()
