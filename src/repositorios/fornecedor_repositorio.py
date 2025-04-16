import questionary
from src.database.conexao import abrir_conexao


def cadastrar(razao_social: str, cnpj: str , nome_fantasia: str ,valor_faturado: int, quantidade_colaboradores: int  ):
    try:
        conexao = abrir_conexao()
        cursor = conexao.cursor()
        cursor.execute("insert into fornecedor (razao_social, cnpj, nome_fantasia , valor_faturado, quantidade_colaboradores) values (%s,%s,%s,%s,%s)",(razao_social,cnpj, nome_fantasia , valor_faturado, quantidade_colaboradores )) 
        conexao.commit()
        conexao.close()
    except Exception as e:
        print(e)


def editar(id_editar: int, razao_social: str, cnpj: str , nome_fantasia: str , valor_faturado: float, quantidade_colaboradores: str):
    try:
        conexao = abrir_conexao()
        cursor = conexao.cursor()
        cursor.execute("""UPDATE fornecedor SET razao_social = %s,cnpj = %s, nome_fantasia = %s,  valor_faturado = %s, quantidade_colaboradores = %s WHERE id = %s""", (razao_social, cnpj, nome_fantasia, valor_faturado, quantidade_colaboradores, id_editar))

        conexao.commit()
        conexao.close()
    except Exception as erro:
        print("Não foi possivel alterar fornecedor!")
        print(erro)


def apagar(id_apagar: int):
    try:
        conexao = abrir_conexao()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM fornecedor WHERE id = %s", (id_apagar,))
        conexao.commit()
        conexao.close()
    except Exception as er:
        print("Não foi possivel apagar o registro")
        print(er)

def listar_todos():
    try:
        conexao = abrir_conexao()
        cursor = conexao.cursor()
        cursor.execute("select id, razao_social, cnpj, nome_fantasia, valor_faturado, quantidade_colaboradores from fornecedor")
        registros = cursor.fetchall()

        fornecedores = []
        for registro in registros:
            fornecedor = {
                "id": registro[0],
                "razao_social": registro[1],
                "cnpj": registro[2],
                "nome_fantasia": registro[3],
                "valor_faturado": registro[4],
                "quantidade_colaboradores": registro[5]
            }
            fornecedores.append(fornecedor)
        return fornecedores
    except Exception as err:
        print("Não foi possivel carregar os fornecedor")
        print(err)
        return[]
        



