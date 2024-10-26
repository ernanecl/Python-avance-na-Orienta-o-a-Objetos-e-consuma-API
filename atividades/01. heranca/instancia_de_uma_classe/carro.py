from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas

    def __str__(self):
        status = "ligado" if self._ligado else "desligado"
        return f'Carro {self.modelo.ljust(10)} | Marca: {self.marca.ljust(10)} | Portas: {str(self.portas).ljust(10)} | Status: {status} ({self._ligado})'