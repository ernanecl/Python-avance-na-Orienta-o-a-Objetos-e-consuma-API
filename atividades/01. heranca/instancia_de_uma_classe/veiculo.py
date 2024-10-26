class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._ligado = False

    def __str__(self):
        status = "ligado" if self._ligado else "desligado"
        return f'Marca: {self.marca} | Veiculo {self.modelo} | Status: {status} ({self._ligado})'