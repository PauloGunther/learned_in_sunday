#CRIAR TABELA DE BINARIO, HEXADECIMAL, COMPLEMENTO DE 1 E OCTAL

"""
Faz conexão com um banco de dados, cria uma tabela, onde de acordo com uma lista 
de valores inteiros os converte para octal, hexadecimal, binario e complemento de 1.
"""
import mysql.connector
import convertion  # Funções de conversão

# Fazer conexao com o banco de dados
cnx = mysql.connector.connect(
    user='root',
    password='root',
    host='localhost',
    database ='aula_sql')

# Criar database e tabela para inserção de dados
cursor = cnx.cursor()
cursor.execute('CREATE DATABASE IF NOT EXISTS aula_sql;')
cursor.execute(
    'CREATE TABLE IF NOT EXISTS exercicio_7 ('
    'name int,'
    'octal_ int,'
    'hex_ varchar(50),'
    'binario_ varchar(40),'
    'complemento_1 varchar(40),'
    'complemento_2 varchar(40))'
        )

# Funçao que converte e insere no bando de dados o valor a ser convertido e suas respectivas conversoes
def inserir_valores(cnx, a):
    y = convertion.to_octal(a)
    x = convertion.to_hex(a)
    z = convertion.to_bin(a)
    v = convertion.to_com1(a)
    
    cursor = cnx.cursor()
    sql = 'INSERT INTO exercicio_7 (name, octal_, hex_, binario_, complemento_1) values (%s, %s, %s, %s, %s)'
    valor = (a, y, x, z, v,)
    cursor.execute(sql, valor)
    cursor.close()

# Lista de valores a serem convertidos e inseridos na tabela
lista = [32768, 12345, 235, 28674, 92]

# Laço para inserção da lista
for i in lista:
    inserir_valores(cnx, i)

cnx.commit()
cursor.close()
cnx.close()
