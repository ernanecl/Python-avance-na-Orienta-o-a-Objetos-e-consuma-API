from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Avaliacao'.ljust(20)} | Status')

        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {str(restaurante.media_avaliacao).ljust(20)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return '⌧ ativo' if self._ativo else '☐ ativo'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        if 0 <= avaliacao._nota <= 5:
            self._avaliacao.append(avaliacao)
            print(f'A avaliacao de {avaliacao._cliente} foi de {avaliacao._nota}')
        else:
            print(f'Avaliacao de nota {avaliacao._nota} nao é valida, {avaliacao._cliente} pode apenas avaliar entre 0 a 5')

    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return 'Sem avaliacao'
        
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_notas = len(self._avaliacao)
        media_notas = round(soma_notas / quantidade_notas,1)

        return media_notas

    def adicionar_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f'Cardapio do restaurante {self._nome}\n')
        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, 'descricao'):
                mensagem_prato = f'{i}. Nome: {item._nome} | Preco: R$ {item._preco:.2f} | Descricao: {item.descricao}'
                print(mensagem_prato)
            elif hasattr(item, 'quantidade'):
                mensagem_bebida = f'{i}. Nome: {item._nome} | Preco: R$ {item._preco:.2f} | Tamanho: {item.tamanho} | Tipo: {item.tamanho} | Descricao: {item.descricao}'
                print(mensagem_bebida)
            else:
                mensagem_bebida = f'{i}. Nome: {item._nome} | Preco: R$ {item._preco:.2f} | Tamanho: {item.tamanho}'
                print(mensagem_bebida)