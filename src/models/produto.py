from typing import Optional


class Produto:
    def __init__(self,nome: str, id:Optional[int] = None):
        self.nome = nome
        self.id = id