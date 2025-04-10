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
# Funções com um/dois underline(s) antes do nome são considerados funções privadas, ou seja, não devem/podem serr utilizadas em outros arquivos.

def __cadastrar():
# Função responsável por cadastar um produto, solicitando os dados necessários para o cadastro.
    nome_produto = input("Digite o nome do produto: ")


    produto_repositorio.cadastrar(nome_produto)
    print("Produto cadastrado com sucesso")




def __listar_todos():
    produtos = produto_repositorio.listar_todos()
    print("lista de produtos: ")
    for produto in produtos:
        print("id:", produto["id"], "nome:", produto["nome"])