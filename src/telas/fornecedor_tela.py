import questionary
from src.repositorios import fornecedor_repositorio

def executar_fornecedor():
    opcoes = ["Listar todos", "Cadastrar", "Editar", "Apagar", "Voltar"]
    opcao_desejada = ""
    opcao_desejada = questionary.select("Escolha o menu desejado", opcoes).ask()
    if opcao_desejada == "Cadastrar":
        __cadastrar_fornecedor()
    elif opcao_desejada == "Listar todos" :
        __listar_fornecedor()
    elif opcao_desejada == "Apagar":
        __apagar_fornecedor()
    elif opcao_desejada == "Editar":
        __editar_fornecedor()

def __cadastrar_fornecedor():
    razao_social = questionary.text("Digite a razão social: ").ask()
    cnpj = questionary.text("Digite o CNPJ: ").ask()
    nome_fantasia = questionary.text("Digite o nome fantasia: ").ask()
    valor_faturado = questionary.text("Digite o valor faturado: ").ask()
    quantidade_colaboradores = questionary.text("Digite a quantidade de colaboradores: ").ask()

    fornecedor_repositorio.cadastrar(razao_social,cnpj,nome_fantasia,valor_faturado,quantidade_colaboradores)
    print("Cadastro realizado com sucesso")

      
def __listar_fornecedor():
    fornecedores = fornecedor_repositorio.listar_todos()
    print("Lista de Fornecedores: ")
    for fornecedor in fornecedores:
        print("id", fornecedor["id"], "razao_social", fornecedor["razao_social"], "cnpj", fornecedor["cnpj"],"nome_fantasia", fornecedor["nome_fantasia"], "valor_faturado", fornecedor["valor_faturado"], "quantidade_colaboradores", fornecedor["quantidade_colaboradores"])






def __apagar_fornecedor():
    id_para_apagar = int(questionary.text("Digite o id para apagar: ").ask())
    fornecedor_repositorio.apagar(id_para_apagar)
    print("Fornecedor apagado com sucesso! ")

def __editar_fornecedor():
    id_para_editar = int(questionary.text("Digite o id para editar: ").ask())
    novo_nome_razão_social = questionary.text("Digite o novo nome da razão social: ").ask()
    novo_cnpj = questionary.text("Digite o novo cnpj: ").ask()
    novo_nome_fantasia = questionary.text("Digite o novo nome fantasia: ").ask()
    novo_valor_faturado = questionary.text("Digite o novo valor faturado: ").ask()
    novo_quantidade_colaboradores = questionary.text("Digite nova quantidade de colaboradores: ").ask()

    fornecedor_repositorio.editar(id_para_editar,novo_nome_razão_social,novo_cnpj,novo_nome_fantasia,novo_valor_faturado ,novo_quantidade_colaboradores)
    print("alterado com sucesso")



