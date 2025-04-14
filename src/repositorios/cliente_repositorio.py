import questionary
from src.database.conexao import abrir_conexao



def cadastrar_cliente(nome_cliente: str):
    try:
        conexao = abrir_conexao()
        cursor = conexao.cursor()

        cursor.execute("insert into clientes (nome) values (%s)", (nome_cliente,))
        
        conexao.commit()
        conexao.close()
    except Exception as erro:
        print(erro)

def listar_todos():
    try:
        conexao = abrir_conexao()
        cursor = conexao.cursor()
        cursor.execute("select id, nome from clientes")
        registros = cursor.fetchall()

        clientes = []
        for registro in registros:
            cliente = {
                "id": registro[0],
                "nome" : registro[1]
            }
            clientes.append(cliente)
        return clientes
    except Exception as err:
        print("Não foi possivel carregar os clientes")
        print(err)




def apagar(id_apagar: int):
    try:
        conexao = abrir_conexao()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM clientes WHERE id = %s", (id_apagar,))
        conexao.commit()
        conexao.close()
    except Exception as er:
        print("Não foi possivel apagar o registro")
        print(er)
    
def editar(id_editar: int, nome: str):
    try:
        conexao = abrir_conexao()
        cursor = conexao.cursor()
        cursor.execute("UPDATE clientes SET nome = %s where id = %s",(nome, id_editar),)
        conexao.commit()
        conexao.close()
    except Exception as erro:
        print("Não foi possivel alterar o produto!")
        print(erro)