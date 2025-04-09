from mysql.connector import connect
nome_produto = input("Digite o nome do produto: ")
if __name__ == "__main__":
    print("Tentando conectar no banco de dados")
    try:
        conexao = connect(
            host="127.0.0.1", # host é a máquina q está o banco de dados
            port=3306, # porta padrão do MySQL
            user="root",
            password="admin",
            database="super_empresa"
        )
        print("Conexão realizada com sucesso")
        # Criar um cursor que nos permitirá executar comandos no banco de dados
        cursor = conexao.cursor()



        # SQL Injection é uma técnica de ataque em que comandos SQL maliciosos são inseridos em entradas 
        # de dados para manipular o banco de dados. Em Python, proteger-se contra SQL Injection é 
        # essencial para evitar vazamento de dados e garantir a segurança de aplicativos web.
        # Como prevenir:
        # update colaboradores set nome = 'Francisco', idade = 31 where id = 10;
        # "update colaboradores set nome = %s, idade = %s where id = %s", (colaborador_nome, idade, id)


        # Definir qual será o comando que iremos executar, neste caso será um insert
        cursor.execute("insert into produtos (nome) values (%s)",(nome_produto,)) 

        # Commit é necessário pois sem ele o insert n será concretizado no bd
        conexao.commit()
        # Fechar a conexão com o bd
        conexao.close()
        print("Produto cadastrado com sucesso")
    except Exception as e:
        print(e)