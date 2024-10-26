from modelos.cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    def __init__(self, nome, preco, tipo, quantidade, descricao):
        super().__init__(nome, preco)
        self.tipo = tipo
        self.tamanho = quantidade
        self.descricao = descricao

    def __str__(self):
        return self._nome
    
    def aplicar_desconto(self):
        self._preco = self._preco * 0.5