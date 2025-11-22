class Produto:
    def __init__(self, id_produto: int, nome: str, preco: float, estoque: int):

        self.id = id_produto
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def __str__(self):
        return f"ID: {self.id} | Nome: {self.nome} | Preço: R$ {self.preco:.2f} | Estoque: {self.estoque}"

    def adicionar_estoque(self, quantidade: int):
        if quantidade > 0:
            self.estoque += quantidade
            return True
        return False

    def subtrair_estoque(self, quantidade: int):
        if 0 < quantidade <= self.estoque:
            self.estoque -= quantidade
            return True
        return False
