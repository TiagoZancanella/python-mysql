import sys
from mysql.connector import connect

def abrir_conexao():
    try:
        conexao = connect(
            host="127.0.0.1", # host é a máquina q está o banco de dados
            port=3306, # porta padrão do MySQL
            user="root",
            password="admin",
            database="super_empresa"
        )
        return conexao
    except Exception as erro:
        print("Não foi possivel realizar a conexão com o bando de dados")
        print(erro)

        sys.exit(1)