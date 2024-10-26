from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de Melancia', 5, 'grande')
prato_pao = Prato('Pao', 2, 'Melhor pao da cidade')
sobremesa_sorvete = Sobremesa('Chocolate', 7, 'Gelado', '100ml', 'Sorvete de chocolate')

bebida_suco.aplicar_desconto()
prato_pao.aplicar_desconto()
sobremesa_sorvete.aplicar_desconto()

restaurante_praca.adicionar_cardapio(bebida_suco)
restaurante_praca.adicionar_cardapio(prato_pao)
restaurante_praca.adicionar_cardapio(sobremesa_sorvete)

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()