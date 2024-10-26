**Exercícios**

01. Crie uma classe chamada Veiculo com um método abstrato chamado ligar.

```PY
from abc import ABC, abstractmethod

class Veiculo1:
    @abstractmethod
    def ligar(self):
        pass
```

&nbsp;

02. No mesmo arquivo, crie um construtor para a classe Veiculo que aceita os parâmetros marca e modelo.

```PY
from abc import ABC, abstractmethod

class Veiculo2:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    @abstractmethod
    def ligar(self):
        pass
```

&nbsp;

03. Crie uma nova classe chamada Carro que herda da classe Veiculo.

```PY
from abc import ABC, abstractmethod

class Veiculo3:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    @abstractmethod
    def ligar(self):
        pass

class Carro3(Veiculo3):
    pass
```

&nbsp;

04. No construtor da classe Carro, utilize o método super() para chamar o construtor da classe pai e atribua o atributo específico cor à classe filha.

```PY
from abc import ABC, abstractmethod

class Veiculo4:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    @abstractmethod
    def ligar(self):
        pass

class Carro4(Veiculo4):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self.cor = cor
```

&nbsp;

05. Em um arquivo chamado main.py, importe a classe Carro.

```BASH
touch main.py
```

**`main.py`**

```PY
from veiculo import Carro
```

&nbsp;

06. No arquivo main.py, instancie três objetos da classe Carro com diferentes características, como marca, modelo e cor.

**`main.py`**

```PY
from veiculo import Carro

carro1 = Carro('Chevrolet', 'Corsa', 'prata')
carro2 = Carro('Ford', 'Focus', 'preto')
carro3 = Carro('Dodge', 'Viper', 'branco')

print(f"Carro 1: {carro1.marca} {carro1.modelo}, Cor: {carro1.cor}")
print(f"Carro 2: {carro2.marca} {carro2.modelo}, Cor: {carro2.cor}")
print(f"Carro 3: {carro3.marca} {carro3.modelo}, Cor: {carro3.cor}")
```
