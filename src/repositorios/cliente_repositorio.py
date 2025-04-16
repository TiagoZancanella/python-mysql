import questionary
from src.database.conexao import abrir_conexao



def cadastrar_cliente(nome_cliente: str , cpf_cliente: str):
    try:
        conexao = abrir_conexao()
        cursor = conexao.cursor()

        cursor.execute("insert into clientes (nome, cpf) values (%s,%s)", (nome_cliente, cpf_cliente))
        
        conexao.commit()
        conexao.close()
    except Exception as erro:
        print(erro)

def listar_todos():
    try:
        conexao = abrir_conexao()
        cursor = conexao.cursor()
        cursor.execute("select id, nome, cpf from clientes")
        registros = cursor.fetchall()

        clientes = []
        for registro in registros:
            cliente = {
                "id": registro[0],
                "nome" : registro[1],
                "cpf" : registro[2]
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
    
def editar(id_editar: int, nome: str, cpf: int):

    try:
        conexao = abrir_conexao()
        cursor = conexao.cursor()
        cursor.execute( "UPDATE clientes SET nome = %s, cpf = %s WHERE id = %s", (nome, cpf, id_editar))
        conexao.commit()
        conexao.close()
    except Exception as erro:
        print("Não foi possivel alterar o cadastro!")
        print(erro)