import questionary
from rich.console import Console
from rich.table import Table
from src.repositorios import produto_repositorio

global produto

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
    produtos = produto_repositorio.listar_todos()

    opcoes_produtos = []
    for produto in produtos:
        opcao = questionary.Choice(title=produto["nome"], value=produto["id"])
        opcoes_produtos.append(opcao)

    id_para_apagar = int(questionary.select("Escolha o produto para apagar", choices=opcoes_produtos).ask())

    confirmacao = questionary.confirm("Deseja realmente apagar o produto?").ask()
    if confirmacao == False:
        return

    produto_repositorio.apagar(id_para_apagar)
    print("Produto apagado com sucesso")


def __editar():

    produtos = produto_repositorio.listar_todos()
    opcoes_produtos = []
    for produto in produtos:
        opcao = questionary.Choice(title=produto["nome"],value=produto["id"])
        opcoes_produtos.append(opcao)
    id_para_editar = int(questionary.select("Escolha o produto para editar: ", choices=opcoes_produtos).ask())
    novo_nome_produtos = questionary.text("Digite o nome do produto: ", validate=__validar_nome).ask().strip()
    produto_repositorio.editar(id_para_editar, novo_nome_produtos)
    print("Produto alterando com sucesso")




def __cadastrar():
    global produtos 
    produtos = produto_repositorio.listar_todos()


# Função responsável por cadastar um produto, solicitando os dados necessários para o cadastro.
    nome_produto = questionary.text("Digite o nome do produto: ",validate=__validar_nome).ask().strip()

    produto_repositorio.cadastrar(nome_produto)
    print("Produto cadastrado com sucesso")
def __listar_todos():
    produtos = produto_repositorio.listar_todos()

    if len(produtos) == 0:
        print("Nenhum produto cadastrado: ")
        return
    

    console = Console()
    tabela = Table()
    tabela.add_column("Código", style="Blue")
    tabela.add_column("Nome", style="Red")


    print("lista de produtos: ")
    for produto in produtos:
        tabela.add_row(

            str(produto["id"]),
            produto["nome"]
        )
    
        console.print(tabela)

def __validar_nome(nome: str):
    global produtos
    for produto in produtos:
        if nome.strip() == produto["nome"]:
            return "Já existe produto cadastrado com este nome"


    if len(nome.strip()) < 3:
        return "Nome do produto deve conter no mínimo 3 caracteres"
    if len(nome.strip()) > 50:
        return "Nome do produto deve conter no máximo 50 caracteres"
    return True

