import questionary
from src.repositorios import cliente_repositorio
# from src.telas.fornecedor_tela import __apagar_fornecedor, __cadastrar_fornecedor, __editar_fornecedor, __listar_todos_fornecedor


def executar_cliente():
    opcoes = ["Listar todos", "Cadastrar", "Editar", "Apagar", "Voltar"]
    opcao_desejada = ""
    while opcao_desejada != "Voltar":
        opcao_desejada = questionary.select("Escolha o menu desejado", opcoes).ask()
        if opcao_desejada == "Cadastrar":
            __cadastrar_cliente()
        elif opcao_desejada == "Listar todos" :
            __listar_todos_cliente()
        elif opcao_desejada == "Apagar":
            __apagar_cliente()
        elif opcao_desejada == "Editar":
            __editar_cliente()



def __cadastrar_cliente():
    nome_cliente = questionary.text("Digite o nome do Cliente: ").ask()
    cpf_cliente = questionary.text("Digite o CPF: ").ask()

    cliente_repositorio.cadastrar_cliente(nome_cliente, cpf_cliente)
    print("Cadastro realizado com sucesso")



def __listar_todos_cliente():
    clientes = cliente_repositorio.listar_todos()
    print("Lista de Clientes: ")
    for cliente in clientes:
        print("id", cliente["id"], "nome", cliente["nome"], "cpf", cliente["cpf"])

        
def __apagar_cliente():
    id_para_apagar = int(questionary.text("Digite o id para apagar: ").ask())
    cliente_repositorio.apagar(id_para_apagar)
    print("Cliente apagado com sucesso! ")

def __editar_cliente():
    id_para_editar = int(questionary.text("Digite o id para editar: ").ask())
    novo_nome_cliente = questionary.text("Digite o novo nome: ").ask()
    novo_cpf_cliente = questionary.text("Digite o novo cpf: ").ask()
    cliente_repositorio.editar(id_para_editar, novo_nome_cliente, novo_cpf_cliente)
    print("alterado com sucesso")



