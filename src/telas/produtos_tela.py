import questionary
from src.repositorios import produto_repositorio


def executar_produto():
    opcoes = ["Listar todos", "Cadastrar", "Editar", "Apagar", "Voltar"]
    opcao_desejada = ""
    while opcao_desejada != "Voltar":
        opcao_desejada = questionary.select("Escolha o menu desejado dos produtos", opcoes).ask()
        if opcao_desejada == "Cadastrar":
            __cadastrar()
        elif opcao_desejada == "Listar todos" :
            __listar_todos()
        elif opcao_desejada == "Apagar":
            __apagar()
        elif opcao_desejada == "Editar":
            __editar()


# Funções com um/dois underline(s) antes do nome são considerados funções privadas, ou seja, não devem/podem serr utilizadas em outros arquivos.


def __apagar():
    id_para_apagar = int(questionary.text("Digite o ID do produto para apagar: ").ask())
    produto_repositorio.apagar(id_para_apagar)
    print("Produto apagado com sucesso")
def __editar():
    id_para_editar = int(questionary.text("Digite o id para editar: ").ask())
    novo_nome_produtos = questionary.text("Digite o nome do produto: ").ask()
    produto_repositorio.editar(id_para_editar, novo_nome_produtos)
    print("Produto alterando com sucesso")
def __cadastrar():
# Função responsável por cadastar um produto, solicitando os dados necessários para o cadastro.
    nome_produto = questionary.text("Digite o nome do produto: ").ask()


    produto_repositorio.cadastrar(nome_produto)
    print("Produto cadastrado com sucesso")
def __listar_todos():
    produtos = produto_repositorio.listar_todos()
    print("lista de produtos: ")
    for produto in produtos:
        print("id:", produto["id"], "nome:", produto["nome"])


            
