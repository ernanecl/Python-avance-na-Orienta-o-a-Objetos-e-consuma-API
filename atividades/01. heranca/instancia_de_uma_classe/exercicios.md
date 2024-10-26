**Exercícios**

01. Crie uma Classe Pai (Veiculo): Implemente uma classe chamada Veiculo com um construtor que aceita dois parâmetros, marca e modelo. A classe deve ter um atributo protegido _ligado inicializado como False por padrão.

```PY
class Veiculo1:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._ligado = False
```

02. Construa o Método Especial str: Adicione um método especial str à classe Veiculo que retorna uma mensagem formatada com a marca, modelo e o estado de ligado/desligado do veículo.

```PY
class Veiculo2:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._ligado = False

    def __str__(self):
        status = "ligado" if self._ligado else "desligado"
        return f'Marca: {self.marca} | Veiculo {self.modelo} | Status: {status} ({self._ligado})'
```

03. Crie uma Classe Filha (Carro): Agora, crie uma classe chamada Carro que herda da classe Veiculo. No construtor da classe Carro, inclua um novo atributo chamado portas que indica a quantidade de portas do carro.

```PY
# veiculo3.py

class Veiculo3:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._ligado = False

    def __str__(self):
        status = "ligado" if self._ligado else "desligado"
        return f'Marca: {self.marca} | Veiculo {self.modelo} | Status: {status} ({self._ligado})'
```

```PY
# carro3.py
from veiculo import Veiculo3

class Carro3(Veiculo3):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas
```

04. Implemente o Método Especial str na Classe Filha: Adicione um método especial str à classe Carro que estenda o método da classe pai (Veiculo) e inclua a informação sobre a quantidade de portas do carro.

```PY
# veiculo4.py

class Veiculo4:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._ligado = False

    def __str__(self):
        status = "ligado" if self._ligado else "desligado"
        return f'Marca: {self.marca} | Veiculo {self.modelo} | Status: {status} ({self._ligado})'
```

```PY
# carro4.py
from veiculo import Veiculo4

class Carro4(Veiculo4):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas

    def __str__(self):
        status = "ligado" if self._ligado else "desligado"
        return f'Carro {self.modelo} | Marca: {self.marca} | Portas: {self.portas} | Status: {status} ({self._ligado})'
```

05. Crie uma Classe Filha (Moto): Similarmente, crie uma classe chamada Moto que também herda de Veiculo. Adicione um novo atributo chamado tipo ao construtor, indicando se a moto é esportiva ou casual.

```PY
# veiculo5.py

class Veiculo5:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._ligado = False

    def __str__(self):
        status = "ligado" if self._ligado else "desligado"
        return f'Marca: {self.marca} | Veiculo {self.modelo} | Status: {status} ({self._ligado})'
```

```PY
# moto5.py
from veiculo import Veiculo5

class Moto5(Veiculo5):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo
```

06. Implemente o Método Especial str na Classe Filha (Moto): Adicione um método especial str à classe Moto que estenda o método da classe pai (Veiculo) e inclua a informação sobre o tipo da moto.

```PY
# veiculo6.py

class Veiculo6:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._ligado = False

    def __str__(self):
        status = "ligado" if self._ligado else "desligado"
        return f'Marca: {self.marca} | Veiculo {self.modelo} | Status: {status} ({self._ligado})'
```

```PY
# moto6.py
from veiculo import Veiculo6

class Moto5(Veiculo6):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo

    def __str__(self):
        status = "ligado" if self._ligado else "desligado"
        return f'Moto {self.modelo} | Marca: {self.marca} | tipo: {self.tipo} | Status: {status} ({self._ligado})'
```

07. Crie um Arquivo Main (main.py): Crie um arquivo chamado main.py no mesmo diretório que suas classes.

```BASH
touch main.py
```

08. Importe e Instancie Objetos: No arquivo main.py, importe as classes Carro e Moto. Em seguida, crie três instâncias de Carro e Moto com diferentes marcas, modelos, quantidade de portas e tipos.

```PY
# main.py
from carro import Carro
from moto import Moto

carro1 = Carro('Chevrolet', 'Corsa', 4)
carro2 = Carro('Ford', 'Focus', 4)
carro3 = Carro('Dodge', 'Viper', 2)

moto1 = Moto('Honda', 'CG 160', 'Casual')
moto2 = Moto('Yamaha', 'Factor 150', 'Casual')
moto3 = Moto('Kawasaki', 'Ninja 400', 'Esportiva')
```

09. Exiba as Informações: Para cada instância, imprima no console as informações utilizando o método str.

```PY
print(carro1)
print(carro2)
print(carro3)

print(moto1)
print(moto2)
print(moto3)
```
