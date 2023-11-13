import mysql.connector
banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="302302",
    database="academiaturmac"
)
meucursor = banco.cursor()
pesquisa = 'select * from alunos;'
meucursor.execute(pesquisa)
resultado = meucursor.fetchall()

for x in resultado:
    print(x)

meucursor.close()

nome1 = "menino ney"
telefone1 = "11111111111"
cpf1 = "18291827161"
endereco1 = "rua do sol"
meucursor = banco.cursor()
sql = ("INSERT INTO alunos (nome, cpf, telefone, endereco) VALUES (%s,%s,%s,%s)")
data = (nome1, telefone1, cpf1, endereco1)
meucursor.execute(sql, data)

banco.commit()
userid = meucursor.lastrowid

print(userid)
