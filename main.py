import os

import questionary

from src.telas.produtos_tela import executar_produto
from src.telas.cliente_tela import executar_cliente


if __name__ == "__main__":
    os.system("cls")
    opcoes = ["Clientes", "Produtos", "Sair"]
    opcao_desejada = ""
    while opcao_desejada != "Sair":
        opcao_desejada = questionary.select("Escolha o menu desejado", opcoes).ask()
       
        if opcao_desejada == "Produtos":
            executar_produto()
        elif opcao_desejada == "Clientes":
            executar_cliente()
        

