from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo

    def __str__(self):
        status = "ligado" if self._ligado else "desligado"
        return f'Moto {self.modelo.ljust(11)} | Marca: {self.marca.ljust(10)} | tipo: {self.tipo.ljust(12)} | Status: {status} ({self._ligado})'