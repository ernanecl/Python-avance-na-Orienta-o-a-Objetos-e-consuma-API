## Python - avance na Orientacao a Objetos e consuma API

O que sera trabalhado durante o treinamento:

- Heranca
- Polimorfismo e metodo abstrato
- Ambientes virtuais
- Requisicoes, json e arquivos
- FastAPI

&nbsp;
&nbsp;

Para esse estudo continuaremos com o projeto desenvolvido no treinamento **Python: aplicando a Orientação a Objetos**.

### 1 Heranca

Neste capitulo foi criado novas *classes* com seus respectivos arquivos.

Segue a arquitetura do sistema atual com os novos itens em **negrito** e o item alterado em *italico*:

* sabor-express
  * *app.py*
  * modelos
    * **cardapio**
      * **bebida.py**
      * **item_cardapio.py**
      * **prato.py**
    * avaliacao.py
    * restaurante.py

&nbsp;

Com isso, seguiremos com os conteudos de cada arquivo:

&nbsp;

**`sabor-express/modelos/cardapio/item_cardapio.py`**

```PY
class ItemCardapio:
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco
```
&nbsp;

**`sabor-express/modelos/cardapio/bebida.py`**

```PY
from modelos.cardapio.item_cardapio import ItemCardapio


class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome,preco)
        self._tamanho = tamanho

    def __str__(self):
        return self._nome
```

&nbsp;

**`sabor-express/modelos/cardapio/prato.py`**

```PY
from modelos.cardapio.item_cardapio import ItemCardapio


class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome,preco)
        self._descricao = descricao

    def __str__(self):
        return self._nome
```

&nbsp;

**`sabor-express/app.py`**

```PY
from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de Melancia', 5, 'grande')
prato_pao = Prato('Pao', 2, 'Melhor pao da cidade')

def main():
    print(bebida_suco)
    print(prato_pao)

if __name__ == '__main__':
    main()
```

&nbsp;

O novo reccurso que trabalhamos entre as classes é a *herança* que possibilita o uso de *atributos* e *métodos* de uma *classe* em outra.

Uma definicao sobre *herança*, é a passada no treinamento da *Alura*, diz o seguinte: '*A herança é um conceito fundamental na programação orientada a objetos (OO) e desempenha um papel crucial no desenvolvimento de software. A importância da *herança* está relacionada à capacidade de criar novas classes reutilizando ou estendendo o comportamento de classes existentes.*'.

&nbsp;

**Herança em Python: Criando Hierarquias de Classes**

***O que é Herança?***

Na programação *orientada a objetos*, a *herança* é um mecanismo que permite que uma *classe* (*classe filha*) herde *atributos* e *métodos* de outra *classe* (*classe pai*). Isso cria uma relação *hierárquica* entre as classes, onde a classe filha é uma especialização da classe pai.

&nbsp;

***Por que usar Herança?***

- **Reutilização de código:** Evita a duplicação de código, pois as **classes filhas** herdam as características da *classe pai*.
- **Organização do código:** Cria uma estrutura *hierárquica* clara, facilitando a compreensão e a manutenção do código.
- **Polimorfismo:** Permite que objetos de diferentes *classes* sejam tratados de forma uniforme, através de *métodos* com o mesmo nome, mas comportamentos diferentes.

&nbsp;

***Como funciona em Python?***

Para criar uma *classe* que *herda* de outra, basta colocar o nome da *classe pai* entre parênteses após o nome da *classe filha*:

```PY
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def comer(self):
        print(f"{self.nome} está comendo.")

class Cachorro(Animal):
    def latir(self):
        print("Au au!")

class Gato(Animal):
    def miar(self):
        print("Miau!")
```

Neste exemplo:

- `Animal` é a *classe pai*.
- `Cachorro` e `Gato` são **classes filhas** que *herdam* de `Animal`.
- `Cachorro` e `Gato` podem acessar e utilizar o *método* `comer` da *classe pai*.
- `Cachorro` e `Gato` possuem seus próprios *métodos* específicos (`latir` e `miar`).

&nbsp;

***Sobreescrita de Métodos:***

Uma *classe filha* pode sobrescrever um *método herdado* da *classe pai*, fornecendo uma implementação diferente:

```PY
class Animal:
    def fazer_som(self):
        print("Fazendo um som genérico.")

class Cachorro(Animal):
    def fazer_som(self):
        print("Au au!")
```

&nbsp;

***Método `super()`:***

O *método* `super()` permite acessar *métodos* da *classe pai* a partir da *classe filha*, mesmo que eles tenham sido sobrescritos:

```PY
class Animal:
    def __init__(self, nome):
        self.nome = nome

class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)
        self.raca = raca
```

&nbsp;

***Herança Múltipla:***

*Python* suporta *herança* múltipla, ou seja, uma *classe* pode *herdar* de múltiplas *classes pais*:

```PY
class Voador:
    def voar(self):
        print("Estou voando!")

class Nadador:
    def nadar(self):
        print("Estou nadando!")

class Pinguim(Voador, Nadador):
    pass
```

&nbsp;

***Quando usar Herança:***

- **Relação "é um":** Se uma *classe* é um tipo específico de outra *classe* (por exemplo, um cachorro é um animal), a *herança* é adequada.
- **Reutilização de código:** Quando precisa de funcionalidades semelhantes em várias *classes*.
- **Criação de hierarquias:** Para organizar o código em uma estrutura *hierárquica* clara.

&nbsp;

***Quando evitar Herança:***

- **Relação "tem um":** Se uma *classe* possui um *atributo* que é outra classe (por exemplo, um carro tem um motor), a composição é mais adequada.
- **Herança profunda:** *Hierarquias* muito profundas podem tornar o código difícil de entender e manter.

&nbsp;

***Em resumo:***

A *herança* é uma ferramenta poderosa em *Python* que permite criar *classes* mais complexas e reutilizáveis. Ao entender os conceitos de *herança*, sobreescrita de *métodos* e *super*, poderá criar designs de software mais eficientes e bem estruturados.

&nbsp;

**Exercícios**

01. Crie uma Classe Pai (Veiculo): Implemente uma classe chamada Veiculo com um construtor que aceita dois parâmetros, marca e modelo. A classe deve ter um atributo protegido _ligado inicializado como False por padrão.

```PY
class Veiculo1:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._ligado = False
```

&nbsp;

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

&nbsp;

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

&nbsp;

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

&nbsp;

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

&nbsp;

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

&nbsp;

07. Crie um Arquivo Main (main.py): Crie um arquivo chamado main.py no mesmo diretório que suas classes.

```BASH
touch main.py
```

&nbsp;

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

&nbsp;

09. Exiba as Informações: Para cada instância, imprima no console as informações utilizando o método str.

```PY
print(carro1)
print(carro2)
print(carro3)

print(moto1)
print(moto2)
print(moto3)
```

&nbsp;
&nbsp;

### 2 Polimorfismo e metodo abstrato

**Topicos do capitulo:**

- Metodos para adicionar itens
- Refatoracao
- Exibindo o cardapio
- Metodos abstrato
- Polimorfismo

&nbsp;

#### OO Sabor Express

Segue a arquitetura do sistema atual com os itens criados ou alterados:

* sabor-express
  * app.py
  * modelos
    * cardapio
      * bebida.py
      * item_cardapio.py
      * prato.py
    * avaliacao.py
    * restaurante.py

&nbsp;

#### 2.1 Metodos para adicionar itens

No arquivo `restaurante.py`, adicionamos os *metodos* `adicionar_bebida_cardapio` e `adicionar_prato_cardapio` na *classe* `Restaurante`.
Tambem adicionamos um novo *atributo* `self._cardapio = []` ao *metodo construtor*.
Para finalizarmos, colocamos duas novas *instancias* no arquivo `app.py`.

&nbsp;

**`sabor-express/modelos/restaurante.py`**

```PY
# ... (resto do código)

class Restaurante:
    # ... (resto do código)

    def __init__(self, nome, categoria):
        # ... (resto do código)
        self._cardapio = []

    # ... (resto do código)
    
    def adicionar_bebida_cardapio(self, bebida):
        self._cardapio.append(bebida)

    def adicionar_prato_cardapio(self, prato):
        self._cardapio.append(prato)
```

&nbsp;

**`sabor-express/app.py`**

```PY
# ... (resto do código)

restaurante_praca.adicionar_bebida_cardapio(bebida_suco)
restaurante_praca.adicionar_prato_cardapio(prato_pao)

# ... (resto do código)
```

&nbsp;

#### 2.2 Refatoracao

A refatoracao feita foi diminuir *metodos* na *classe* `Restaurante`, eliminando os *metodos* `adicionar_bebida_cardapio` e `adicionar_prato_cardapio` para adicionar o *metodo* `adicionar_cardapio`.

&nbsp;

**`sabor-express/modelos/restaurante.py`**

```PY
# ... (resto do código)
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    # ... (resto do código)

    def adicionar_cardapio(self, item): # Esse método é responsável por adicionar um item ao cardápio do restaurante.
        if isinstance(item, ItemCardapio): # Verificação de Tipo: Antes de adicionar o item ao cardápio, o código verifica se o objeto passado como argumento (item) é uma instância da classe ItemCardapio. Isso garante que apenas objetos do tipo ItemCardapio possam ser adicionados ao cardápio, evitando erros e mantendo a integridade dos dados.
            self._cardapio.append(item) # Se o objeto passado for do tipo ItemCardapio, ele é adicionado a uma lista chamada _cardapio que armazena os itens do cardápio do restaurante.
```

&nbsp;

**Benefícios e Conceitos Utilizados**

- **Polimorfismo:** A verificação `isinstance(item, ItemCardapio)` demonstra o *polimorfismo*. O *método* `adicionar_cardapio` pode aceitar qualquer objeto que seja uma *instância* de `ItemCardapio` ou de uma subclasse de `ItemCardapio`, permitindo flexibilidade na criação de diferentes tipos de itens de cardápio.
- **Tipagem de Dados:** Ao verificar o tipo do objeto, o código garante a integridade dos dados e evita erros. Isso torna o código mais robusto e fácil de manter.
- **Encapsulamento:** O uso do underscore (`_`) no nome do atributo `_cardapio` indica que ele é privado e não deve ser acessado diretamente de fora da *classe*, promovendo o encapsulamento e a proteção dos dados internos da *classe*.

&nbsp;

**`sabor-express/app.py`**

```PY
# ... (resto do código)

restaurante_praca.adicionar_cardapio(bebida_suco)
restaurante_praca.adicionar_cardapio(prato_pao)

# ... (resto do código)
```

&nbsp;

#### 2.3 Exibindo o cardapio

Foi criado uma *classe* `exibir_cardapio`, nela usamos o *parametro especial* `self`, como o laco de repeticao `for` e a condicional `if/else`, tambem usou as novas funcoes `enumerate` e `hasattr`.

&nbsp;

**`sabor-express/modelos/restaurante.py`**

```PY
# ... (resto do código)

    @property
    def exibir_cardapio(self):
        print(f'Cardapio do restaurante {self._nome}\n')
        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, 'descricao'):
                mensagem_prato = f'{i}. Nome: {item._nome} | Preco: R$ {item._preco:.2f} | Descricao: {item.descricao}'
                print(mensagem_prato)
            else:
                mensagem_bebida = f'{i}. Nome: {item._nome} | Preco: R$ {item._preco:.2f} | Tamanho: {item.tamanho}'
                print(mensagem_bebida)
```

&nbsp;

**Analisando o Código**

***O Decorador `@property`***

- **O que faz:** Transforma um *método* em uma *propriedade*. Isso significa que pode acessar o *método* como se fosse um *atributo*, sem a necessidade de usar *parênteses*.
- **Por que usar:** Aumenta a legibilidade do código, tornando-o mais parecido com a forma como acessamos *atributos*.
- **Neste caso:** O *método* `exibir_cardapio` está sendo transformado em uma *propriedade*, permitindo que seja acessado como `restaurante.exibir_cardapio`.

***Método `exibir_cardapio`***

- **`print(f'Cardapio do restaurante {self._nome}\n')`:** A primeira linha, imprime o nome do restaurante, usando o atributo `_nome` da *instância*.
- **`for i, item in enumerate(self._cardapio, start=1)`:** O `for` *loop* itera pelos os itens do cardápio (`self._cardapio`), numerando-os a partir de *1*.
- **Verificação do tipo de item:**
    - **`if hasattr(item, 'descricao')`:** Se tiver atributo `descricao`, é considerado um *prato* e a mensagem é formatada com *nome*, *preço* e *descrição*.
    - **`else`**: Caso contrário, é considerado uma *bebida* e a mensagem é formatada com *nome*, *preço* e *tamanho*.
- **Formatação da saída:** As *f-strings* são usadas para formatar as mensagens de forma clara e concisa, com o preço formatado com duas casas decimais.

***Resumo do Funcionamento***

- Ao chamar `restaurante.exibir_cardapio`, o *método* é executado.
- O *método* imprime o nome do *restaurante*.
- Para cada *item no cardápio*, ele verifica se o *item* é um *prato* ou uma *bebida* com base na existência do *atributo descricao*.
- Imprime uma mensagem formatada para cada *item*, mostrando o número, nome, preço e, dependendo do *tipo*, descrição ou tamanho.

&nbsp;

**Novas funcoes usadas no codigo**

***`for i, item in enumerate(self._cardapio, start=1):`***

***`enumerate()`:*** Essa *função* é muito útil quando precisa iterar sobre uma sequência (como uma *lista*, *tupla* ou *string*) e, ao mesmo tempo, ter acesso ao índice de cada elemento. Ela retorna um objeto *enumerador* que gera pares (*índice*, *elemento*) a cada iteração.

- **`i`:** Recebe o *índice* atual do elemento na iteração.
- **`item`:** Recebe o elemento da lista `self._cardapio` na posição correspondente ao índice.
- **`start=1`:** Especifica que a contagem dos índices deve começar em 1, em vez do 0 padrão. Isso significa que o primeiro elemento terá o índice 1, o segundo terá o índice 2, e assim por diante.

&nbsp;

***`if hasattr(item, 'descricao'):`***

***`hasattr()`:*** Essa *função* verifica se um objeto possui um determinado *atributo*. Ela retorna `True` se o objeto tiver o *atributo* especificado e `False` caso contrário.

- **`item`:** O objeto que será verificado.
- **`'descricao':`** O nome do atributo que queremos verificar.

#### 2.4 Metodos abstrato

Implementado o *metodo abstrado* no arquivo `item_cardapio.py`.

**`sabor-express/modelos/cardapio/item_cardapio.py`**

```PY
from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    @abstractmethod
    def aplicar_desconto(self):
        pass
```

&nbsp;

***Analisando o Código Python***

- **`Importação:`** A linha `from abc import ABC, abstractmethod` importa as *classes* `ABC` e o *decorador* `abstractmethod` do *módulo* `abc` *(Abstract Base Class)*, que são essenciais para definir *classes* e *métodos abstratos* em *Python*.
- **Classe abstrata `ItemCardapio`:**
    - Herda da *classe* `ABC`, indicando que é uma *classe abstrata*.
    - Possui um *método construtor* `__init__` que inicializa os *atributos* `_nome` e `_preco` de um item de cardápio.
    - Possui um *método abstrato* `aplicar_desconto`. Esse *método* não tem implementação, apenas define a assinatura.

&nbsp;

***O que esse código significa?***

- A *classe* `ItemCardapio` define um modelo genérico para qualquer item de um cardápio.
- O método `aplicar_desconto` indica que todos os itens de cardápio podem ter um desconto aplicado, mas a forma como esse desconto será calculado e aplicado varia de acordo com o tipo de item (pizza, bebida, etc.).
- As *classes filhas* de `ItemCardapio` (por exemplo, Pizza, Bebida) deverão implementar o *método* `aplicar_desconto` para definir a lógica específica de cálculo de desconto para cada tipo de item.

&nbsp;

***Exemplo de uso***

```PY
class Pizza(ItemCardapio):
    def aplicar_desconto(self):
        # Lógica específica para calcular o desconto de uma pizza
        novo_preco = self._preco * 0.9  # Desconto de 10%
        return novo_preco

class Bebida(ItemCardapio):
    def aplicar_desconto(self):
        # Lógica específica para calcular o desconto de uma bebida
        # ...
```

&nbsp;

***Em resumo:***

O código define uma estrutura para representar itens de um cardápio, onde cada item pode ter um desconto, mas a forma de calcular esse desconto é definida pelas *classes filhas*. Isso torna o código mais flexível e reutilizável, pois permite criar diferentes tipos de itens com suas próprias regras de desconto.

&nbsp;

***Métodos Abstratos e o Código Python***

***O que é um Método Abstrato?***

Em programação *orientada a objetos*, um *método abstrato* é um *método* declarado em uma *classe abstrata*, mas que não possui uma implementação concreta. Ou seja, ele apenas define a assinatura do *método* (nome, parâmetros e tipo de retorno), mas deixa a implementação específica para as *classes filhas*.

&nbsp;

***Características de um Método Abstrato:***

- **Não tem corpo:** A declaração do *método* termina com um ponto e vírgula, sem as chaves que delimitam o corpo de um *método* normal.
- **É precedido pela palavra-chave `abstract`:** Essa palavra-chave indica que o *método* é *abstrato* e não tem implementação na classe pai.
- **Obriga as *classes filhas* a implementarem:** As classes que herdam da *classe abstrata* são obrigadas a implementar o *método abstrato*, cada uma à sua maneira, de acordo com sua lógica específica.

&nbsp;

***Por que usar métodos abstratos?***

- **Abstração:** Permite criar *classes* mais genéricas, definindo uma interface comum para as *classes filhas*.
- **Polimorfismo:** Permite que diferentes *classes filhas* tenham implementações diferentes para o mesmo *método*, tornando o código mais flexível e reutilizável.
- **Hierarquias de classes:** Ajuda a organizar o código em uma hierarquia de *classes*, onde a *classe abstrata* define as características comuns e as *classes filhas* as particularidades.


&nbsp;

#### 2.5 Polimorfismo

Aplicacao dos metodos `aplicar_desconto` nas classes `Prato` e `Bebidas`, tambem teve a aplicacao do uso do metodo no  arquivo `app.py`.

**`sabor-express/modelos/cardapio/bebida.py`**

```PY
# ... (resto do código)

    def aplicar_desconto(self):
        self._preco = self._preco * 0.75
        return self._preco
```

&nbsp;

**`sabor-express/modelos/cardapio/prato.py`**
```PY
# ... (resto do código)

    def aplicar_desconto(self):
        self._preco = self._preco * 0.9 
        return self._preco
```

&nbsp;

**`sabor-express/modelos/cardapio/prato.py`**

```PY
bebida_suco.aplicar_desconto()
prato_pao.aplicar_desconto()
```

&nbsp;

***Polimorfismo em Python: Uma Explicação Simples***

***O que é Polimorfismo?***

Em programação *orientada a objetos*, *polimorfismo* significa a capacidade de um objeto assumir muitas formas. Em outras palavras, um mesmo *método* pode se comportar de maneira diferente em diferentes *classes*, dependendo do contexto. Isso torna o código mais flexível e reutilizável.

&nbsp;

***Polimorfismo em Python:***

Em *Python*, o *polimorfismo* é alcançado principalmente através da *herança* e da sobrecarga de *métodos*.

- **Herança:** Quando uma *classe* herda de outra, ela adquire os *métodos* e *atributos* da *classe pai*. No entanto, a *classe filha* pode sobrescrever esses *métodos*, implementando uma lógica diferente.
- **Sobrecarga:** É o processo de criar *métodos* com o mesmo nome, mas com diferentes *parâmetros*, em uma mesma classe ou em classes diferentes.

&nbsp;

***Exemplo Prático:***

Imagine uma *classe* base chamada `Animal` e duas *classes filhas*, `Cachorro` e `Gato`. Ambas as *classes filhas* herdam da *classe* base e possuem um *método* chamado `fazer_barulho()`. No entanto, a implementação desse *método* será diferente para cada classe:

```PY
class Animal:
    def fazer_barulho(self):
        pass

class Cachorro(Animal):
    def fazer_barulho(self):
        print("Au au!")

class Gato(Animal):
    def fazer_barulho(self):
        print("Miau!")
```

Nesse exemplo, o *método* `fazer_barulho()` é *polimórfico*, pois ele se comporta de maneira diferente dependendo do objeto que o chama. Se criar um objeto `cachorro` e chamar o *método* `fazer_barulho()`, ele irá imprimir "Au au!". Se criar um objeto `gato` e chamar o mesmo *método*, ele irá imprimir "Miau!".

&nbsp;

***Por que usar Polimorfismo?***

- **Reutilização de código:** Ao criar uma *classe* base, pode definir *métodos* comuns que serão herdados por todas as *classes filhas*.
- **Flexibilidade:** O *polimorfismo* permite que você trate *objetos* de diferentes *classes* de forma uniforme, tornando o código mais flexível e fácil de manter.
- **Abstração:** O *polimorfismo* ajuda a criar abstrações mais poderosas, permitindo que concentre na interface dos *objetos*, em vez de suas implementações específicas.

&nbsp;

***Outro Exemplo: Formas Geométricas***

```PY
class Forma:
    def area(self):
        pass

class Retangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return 3.14159 * self.raio**2

```

Neste exemplo, o *método* `area()` é *polimórfico*. A implementação específica do *método* `area()` varia dependendo se o *objeto* é um retângulo ou um círculo.

&nbsp;

***Em resumo:***

O *polimorfismo* é uma característica fundamental da programação *orientada a objetos* que permite escrever código mais flexível, reutilizável e fácil de entender. Ao entender o *polimorfismo*, estará mais preparado para criar programas mais robustos e escaláveis.


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

&nbsp;
&nbsp;

### 3 Ambientes Virtuais

*Ambientes virtuais* são essenciais para organizar projetos *Python* e evitar conflitos de dependências, isolando o projeto. O *Poetry* é uma ferramenta mais completa e recomendada para a maioria dos projetos, enquanto o *venv* é uma opção mais básica para projetos simples.

&nbsp;

#### 3.1 Venv - Ambiente Virtual Python

Nesse capitulo vamos trabalhar com a ferramenta `venv`, ele é uma ferramenta padrao do Python e nao tem a necessidade de instalar para uso.

Vamos criar um novo diretorio e acessa-lo, com os comandos abaixo:

```BASH
mkdir virtual_environment
cd virtual_environment
```

&nbsp;

Em seguida para criar o *ambiente virtual*, vamos executar o seguinte comando:

```BASH
# python: Indica que você está executando o interpretador Python.
# -m: Essa flag indica que você está executando um módulo Python como um script.
# venv: É o nome do módulo padrão do Python que cria ambientes virtuais.
# environment_name: É o nome que você escolherá para o seu ambiente virtual.
python -m venv environment_name
```

&nbsp;

**Explicação detalhada:**

- **`python -m`:** Ao usar `-m`, você está dizendo ao *Python* para tratar o *módulo* `venv` como um *script* principal. Isso significa que o *Python* irá executar o código dentro do *módulo* `venv` como se fosse um programa independente.
- **`venv`**: O *módulo* `venv` é parte da biblioteca padrão do *Python* e fornece a funcionalidade para criar e gerenciar *ambientes virtuais*. Ao executar `python -m venv`, você está iniciando esse *módulo*.
- **`environment_name`:** Este é o nome que você dará ao seu *ambiente virtual*. É importante escolher um nome descritivo para facilitar a identificação.

&nbsp;

Apos a execucao do comando é criado diretorios e arquivos, como mostrado abaixo:

* virtual_environment
  * venv
    * bin
        * activate
        * activate.csh
        * activate.fish
        * Activate.ps1
        * pip
        * pip3
        * pip3.12
        * python
        * python3
        * python3.12
    * include/python3.12
    * lib/python3.12/site-packages
        * pip/...
        * pip-24.0.dist-info/...
    * lib64/python3.12/site-packages
        * pip/...
        * pip-24.0.dist-info/...
    * pyvenv.cfg

&nbsp;

**Diretórios Principais e suas Funcionalidades:**

- **`bin`:**
    - **`activate`:** *Scripts* para ativar o *ambiente virtual* em diferentes *shells* (*Bash*, *Zsh*, *Fish*, *PowerShell*). Ao ativar o ambiente, você modifica as variáveis de ambiente para que o *Python* use os executáveis e bibliotecas do *ambiente virtual*, em vez dos globais.
    - **`pip`, `pip3`, `python`, `python3`:** *Links* simbólicos (ou atalhos) para os executaveis do *Python* e do gerenciador de pacotes *pip* dentro do *ambiente virtual*.
    - **Versões específicas (`pip3.12`, `python3.12`):** Podem existir caso você tenha instalado versões específicas do Python ou pip.
- **`include/python3.12`:** Contém os cabeçalhos de arquivos *C* usados para compilar extensões *Python*. Se você precisar compilar uma extensão para o seu projeto, os arquivos nesse diretório serão utilizados.
- **`lib/python3.12/site-packages`:** Este é o diretório principal onde os pacotes *Python* instalados no *ambiente virtual* são armazenados. Os pacotes são organizados em subdiretórios.
- **`lib64/python3.12/site-packages`:** Em sistemas de *64 bits*, este diretório pode ser usado para armazenar bibliotecas compartilhadas maiores. A sua presença e conteúdo podem variar dependendo da distribuição *Linux* e da configuração do ambiente.
- **`pyvenv.cfg`:** Este arquivo de configuração contém informações sobre o *ambiente virtual*, como a localização da instalação do *Python* usada para criar o ambiente e o diretório de isolamento.

&nbsp;

**Resumindo:**
- **`bin`:** Contém os scripts e executáveis necessários para usar o ambiente virtual.
- **`include`:** Armazena os cabeçalhos C para a compilação de extensões Python.
- **`lib` e `lib64`:** Armazenam os pacotes Python instalados e as bibliotecas compartilhadas.
- **`pyvenv.cfg`:** Configurações do ambiente virtual.

&nbsp;

**Ativando ambiente virtual `venv`**

Acessando o diretorio do ambiente virtual, executamos o comando de ativar de acordo com o sistema operacional usado.

Ambiente *Linux*

```BASH
source venv/bin/activate
```

Ambiente *Windows*

```BASH
venv\Scripts\activate.bat
```

&nbsp;

**Desativando ambiente virtual `venv`**

Tambem dentro do diretorio, seguimos com o comando abaixo para desativar o ambiente.

Ambiente *Linux* e *Windows*

```BASH
deactivate
```

&nbsp;

#### 3.2 Criando o `Requirements.txt`

**Instalação de bibliotecas e isolamento de dependências**

Para instalar *bibliotecas*, utilizamos o mesmo processo que realizamos para instalar qualquer coisa com o `pip`. No terminal, passamos `pip install` seguido do nome da *biblioteca* ou *módulo*, nesse caso `requests`.

```BASH
pip install requests
```

O `pip` é um gerenciador de *módulos* e pacotes do *Python*. A maioria das linguagens tem um gerenciador que auxilia nisso.

No caso do *Python*, existe mais de um, mas o `pip` é o mais conhecido. Quando usamos `pip install` ou `pip uninstall` para instalar ou desinstalar um pacote, só então passamos o nome do pacote.

O pip vem por padrão quando instalamos o Python na máquina.

&nbsp;

Comando para verificar os pacotes instalados no ambiente.

```BASH
pip freeze
```

&nbsp;

Comando para enviar saida do comando `pip freeze` para o arquivo `requirements.txt`.

Executar no diretorio raiz do projeto.

```BASH
pip freeze > requirements.txt
```

&nbsp;
&nbsp;

### 4 Requests, JSON and files

#### 4.1 API

**O que é uma API?**

*API* significa *Interface de Programação de Aplicações* (*Application Programming Interface*). Em termos simples, é um conjunto de regras e especificações que permite que diferentes softwares se comuniquem e troquem informações entre si. Imagine uma *API* como um menu em um restaurante: você (o programa) faz um pedido (a *requisição*), o garçom (a *API*) leva o pedido para a cozinha (o *servidor*) e traz de volta o prato pronto (a *resposta*).

&nbsp;

**Por que as APIs são importantes?**

- **Reutilização de código:** Em vez de reescrever funcionalidades do zero, pode utilizar *APIs* já existentes.
- **Integração de sistemas:** Permite que diferentes sistemas se conectem e trabalhem em conjunto.
- **Desenvolvimento mais rápido:** Acelera o processo de desenvolvimento, pois pode se concentrar em funcionalidades específicas.
- **Acesso a dados e serviços:** Permite que acesse dados e serviços de outras empresas, como mapas, previsão do tempo, etc.

&nbsp;

**APIs em Python**

*Python*, com sua sintaxe clara e concisa, é uma linguagem excelente para criar e consumir *APIs*. A comunidade *Python* oferece diversas bibliotecas e *frameworks* que facilitam o desenvolvimento de *APIs*, como:

- **Flask:** Um *microframework* leve e flexível, ideal para criar *APIs* pequenas e médias.
- **Django REST framework:** Um *framework* poderoso e completo para construir *APIs RESTful* em larga escala.
- **FastAPI:** Um *framework* moderno e *high-performance*, com foco em desenvolvimento rápido e conciso.

&nbsp;

**Por que usar Python para APIs?**

- **Facilidade de uso:** A sintaxe do *Python* é clara e intuitiva, facilitando o aprendizado e o desenvolvimento.
- **Grande comunidade:** A comunidade *Python* é vasta e oferece diversas bibliotecas e recursos para desenvolvimento de *APIs*.
- **Versatilidade:** *Python* pode ser utilizado para criar *APIs* de diversos tipos, desde simples *APIs RESTful* até *APIs* mais complexas com funcionalidades avançadas.
- **Integração com outras tecnologias:** *Python* se integra facilmente com outras tecnologias, como bancos de dados, sistemas de filas e serviços em nuvem.

&nbsp;

**Exemplo simples de uma API em Python usando Flask:**

```PY
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
```

Este código cria uma *API* simples que retorna a mensagem `Hello, World!` quando acessada.

&nbsp;

**Conceitos importantes em APIs Python:**

- **Requisições HTTP:** As *APIs* geralmente usam o protocolo *HTTP* para se comunicar. As requisições *HTTP* mais comuns são *GET*, *POST*, *PUT* e *DELETE*.
- **Respostas HTTP:** As *APIs* retornam respostas *HTTP* com um código de status (por exemplo, *200* para *sucesso*) e um corpo (dados em formato *JSON* ou *XML*).
- **Rotas:** As rotas definem os endereços (*URLs*) que podem ser acessados na *API*.
- **Recursos:** Os recursos são os objetos que a *API* expõe, como usuários, produtos, etc.
- **Métodos HTTP:** Os *métodos HTTP* (*GET*, *POST*, *PUT*, *DELETE*) são usados para realizar operações nos recursos.

&nbsp;

**Em resumo:**

As *APIs* são uma parte fundamental do desenvolvimento de *software* moderno. *Python*, com sua sintaxe simples e rica ecossistema, é uma excelente escolha para criar *APIs* robustas e escaláveis. Ao aprender sobre *APIs* em *Python*, você estará abrindo portas para um mundo de possibilidades, desde a criação de aplicativos web até a integração de sistemas complexos.

&nbsp;

#### 4.2 Requisicao - Request

Nesta etapa trabalhamos com a boblioteca `request` para buscar dados de uma *URL* com a funcao *GET*. 

Dentro do ambiente virtual criamos um arquivo com nome `app.py`.

**`virtual_environment/app.py`**

```PY
import requests # Importando a biblioteca requests para realizar requisições HTTP

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'  # URL da API que contém os dados dos restaurantes
response = requests.get(url)  # Fazendo uma requisição GET para a URL e armazenando a resposta em 'response'

print(response)  # Imprimindo a resposta completa (para fins de depuração)

if response.status_code == 200:  # Verificando se a requisição foi bem-sucedida (código de status 200)
    dados_json = response.json()  # Convertendo a resposta JSON para um dicionário Python
    print(dados_json) # Imprimindo a resposta JSON ema um dicionário Python
else:
    print(f'O erro foi {response.status_code}')  # Imprimindo o código de status do erro caso a requisição falhe
```

Se executarmos o codigo sem a condicional `if`/`else` para testar a *URL*, aguardamos um retorno `<Response [200]>`.

&nbsp;

**A Biblioteca Requests do Python: Sua Porta de Entrada para o Mundo das APIs**

A biblioteca *Requests* é uma ferramenta poderosa e fácil de usar em *Python*, especialmente projetada para simplificar a interação com *APIs* e serviços *web*. Com ela, podemos realizar requisições *HTTP* de forma intuitiva e eficiente, sem se preocupar com os detalhes técnicos da comunicação entre sistemas.

&nbsp;

**Por que usar a biblioteca Requests?**

- **Sintaxe simples e clara:** A sintaxe da *Requests* é muito semelhante à forma como fazemos solicitações na *web*, tornando o código mais legível e fácil de entender.
- **Versatilidade:** Permite realizar todos os tipos de requisições *HTTP* (*GET*, *POST*, *PUT*, *DELETE*, etc.), além de lidar com *headers*, *cookies*, *autenticação* e muito mais.
- **Gerenciamento de respostas:** Facilita o processamento das respostas, permitindo acessar o conteúdo, os *headers* e o *status* da requisição.
- **Extensibilidade:** Pode ser facilmente estendida com *plugins* para adicionar funcionalidades personalizadas.

&nbsp;

**Como funciona a Requests?**

A ideia básica é simples: você cria um objeto de requisição e envia para um determinado *URL*. A resposta é então retornada como um objeto que podemos analisar.

Exemplo:

```PY
import requests

response = requests.get('https://api.github.com/users/ernanecl')
print(response.json())
```

Neste exemplo, fazemos uma requisição *GET* para a *API* do *GitHub* para obter informações sobre o usuário "ernanecl". A resposta é um objeto *JSON* que contém os dados do usuário.

&nbsp;

**Principais funcionalidades da Requests:**

- **Métodos HTTP:** *GET*, *POST*, *PUT*, *DELETE*, *HEAD*, *OPTIONS*
- **Parâmetros de consulta:** Adiciona parâmetros à *URL* da requisição
- **Dados de formulário:** Envia dados em formulários
- **Headers:** Define cabeçalhos personalizados
- **Cookies:** Manipula *cookies*
- **Autenticação:** Suporta diversos mecanismos de *autenticação* (*basic*, *digest*, *OAuth*, etc.)
- **Timeout:** Define um tempo limite para as requisições
- **Proxy:** Utiliza *proxies* para fazer as requisições

&nbsp;

**Casos de uso comuns:**

- **Consumir APIs:** Interagir com *APIs* de serviços como o *GitHub*, *Twitter*, *Google Maps*, etc.
- **Testar APIs:** Verificar se uma *API* está funcionando corretamente e retornar os dados esperados.
- **Automatizar tarefas:** Realizar tarefas repetitivas, como coletar dados de um site ou fazer login em um sistema.
- **Raspagem de dados:** Extrair dados de sites *HTML*.

&nbsp;

**Em resumo:**

A biblioteca *Requests* é uma ferramenta essencial para qualquer desenvolvedor *Python* que precise interagir com *APIs* e serviços *web*. Sua simplicidade, flexibilidade e extensibilidade a tornam uma escolha popular para uma ampla gama de aplicações.

&nbsp;

#### 4.3 Filtrando dados

```PY
# ... (resto do código)

if response.status_code == 200:  # Verificando se a requisição foi bem-sucedida (código de status 200)
    # ... (resto do código)
   dados_restaurante = {}  # Criando um dicionário para armazenar os dados dos restaurantes, organizados por nome

    # Iterando sobre os dados JSON
    for item in dados_json: 
        nome_do_restaurante = item['Company'] # Obtendo o nome do restaurante a partir do item atual

        # Verificando se o restaurante já existe no dicionário
        if nome_do_restaurante not in dados_restaurante:
            # Se não existe, cria uma nova entrada no dicionário
            dados_restaurante[nome_do_restaurante] = []

        # Adiciona um novo item ao restaurante no dicionário
        dados_restaurante[nome_do_restaurante].append({
            "item": item['Item'],
            "price": item['price'],
            "description": item['description']
        })

    print(dados_restaurante)  # Imprimindo o dicionário final com os dados dos restaurantes organizados por nome
# ... (resto do código)
```

**Explicações adicionais:**

- **`dados_restaurante`:** Esse dicionário está sendo usado para agrupar os itens de cada restaurante. As chaves do dicionário são os nomes dos restaurantes, e os valores são listas de dicionários, onde cada dicionário representa um item do menu.
- **`if nome_do_restaurante not in dados_restaurante`:** Essa condição verifica se o nome do restaurante atual já existe como uma chave no dicionário dados_restaurante. Se não existir, uma nova entrada é criada.
- **`dados_restaurante[nome_do_restaurante].append(...)`:** Essa linha adiciona um novo item ao final da lista correspondente ao restaurante atual. O novo item é um dicionário com as informações do item do menu.

&nbsp;

**Por que `dados_json = response.json()` cria um dicionário?**

Para entendermos por que a linha `dados_json = response.json()` converte a resposta da *API* em um *dicionário*, precisamos entender um pouco sobre como os dados são estruturados e transmitidos pela internet.

&nbsp;

**JSON: A Linguagem dos Dados na Web**

- **JSON (JavaScript Object Notation):** É um formato leve para troca de dados, que se baseia em pares chave-valor. Ele é amplamente utilizado para transmitir dados entre um servidor e um cliente, como em *APIs REST*.
- **Estrutura:** *JSON* utiliza chaves *{}* para delimitar objetos (similares a *dicionários* em *Python*) e colchetes *[]* para delimitar arrays (similares a *listas* em *Python*).

&nbsp;

**O Método `.json()`**

- **Conversão:** O método `.json()` do objeto `response` é responsável por converter a string *JSON* retornada pela *API* em uma estrutura de dados *Python* equivalente.
- **Dicionário:** Como a estrutura básica do *JSON* é muito similar a um dicionário em *Python*, a forma mais natural de representar um objeto *JSON* em *Python* é utilizando um dicionário.

&nbsp;

**Entendendo a Linha de Código `dados_restaurante[nome_do_restaurante] = []`**

**O que essa linha faz:**

- **`dados_restaurante[nome_do_restaurante] = []`:** Essa linha está *criando uma nova chave* no *dicionário* `dados_restaurante` e associando a ela uma lista vazia.

&nbsp;

**Por que uma lista e não um dicionário?**

- **Organização dos dados:** A ideia aqui é agrupar todos os itens de um mesmo restaurante em uma lista. Cada item do menu será um dicionário dentro dessa lista.
- **Flexibilidade:** Utilizar uma lista permite adicionar novos itens ao restaurante de forma simples, apenas adicionando novos dicionários à lista.

&nbsp;

**Por que o `nome_do_restaurante` antes do `=`?**

- **Acesso a um elemento específico:** Quando você utiliza colchetes `[]` após o nome do dicionário, você está acessando ou criando um elemento com a chave especificada dentro daquele dicionário.
- **Criação de uma nova chave:** Se a chave ainda não existir, ela será criada e o valor à direita do `=` será atribuído a ela.

&nbsp;

Exemplo prático:

Imagine que o primeiro restaurante encontrado seja "Restaurante X". Após executar essa linha, o dicionário `dados_restaurante` ficará assim:

```PY
dados_restaurante = {
    "Restaurante X": []
}
```

&nbsp;

**Por que não `dados_restaurante = {nome_do_restaurante}`?**

- **Sobrescrita do dicionário:** Se você fizesse dados_restaurante = {nome_do_restaurante}, você estaria substituindo todo o dicionário por um novo dicionário com apenas uma chave. Isso faria com que você perdesse todos os dados já adicionados anteriormente.
- **Estrutura inadequada:** A ideia é ter um dicionário onde as chaves são os nomes dos restaurantes e os valores são listas de itens. Criar um dicionário com apenas uma chave e um valor não atenderia a essa necessidade.

&nbsp;

**Em resumo:**

- **Criando uma nova chave:** Ao utilizar `dados_restaurante[nome_do_restaurante] = []`, você está criando uma nova chave no dicionário `dados_restaurante`.
- **Associando uma lista:** O valor associado a essa nova chave é uma lista vazia, que servirá para armazenar os itens do restaurante.
- **Flexibilidade:** A utilização de uma lista permite adicionar novos itens ao restaurante de forma simples e organizada.

&nbsp;

**Para visualizar melhor:**

```PY
# Após várias iterações do loop
dados_restaurante = {
    "Restaurante X": [
        {"item": "Pizza", "price": 25.99},
        {"item": "Macarrão", "preco": 19.99}
    ],
    "Restaurante Y": [
        {"item": "Hambúrguer", "price": 15.99},
        {"item": "Batata frita", "preco": 8.99}
    ]
}
```

Como você pode ver, cada restaurante tem sua própria lista de itens, permitindo uma organização eficiente dos dados.

&nbsp;

#### 4.4 Criando arquivos com Python

```PY
# ... (resto do código)
import json # Importando o modulo json para trabalhar com dados em formato JSON

# ... (resto do código)

# Iteração sobre o dicionário: Inicia um loop for para percorrer todas as chaves e valores do dicionário dados_restaurante.
# Desempacotamento: A cada iteração, a chave (nome do restaurante) é atribuída à variável nome_do_restaurante e o valor (lista de itens) é atribuído à variável dados.
for nome_do_restaurante, dados in dados_restaurante.items():
    nome_do_arquivo = f'{nome_do_restaurante}.json' # string formatada (f-string) para o nome do arquivo, usando o nome do restaurante como base e adicionando a extensão .json
    # Abre um arquivo para escrita ('w') com o nome gerado anteriormente.
    # Gerenciamento de recursos: O with garante que o arquivo seja fechado corretamente, mesmo que ocorra alguma exceção.
    with open(nome_do_arquivo,'w') as arquivo_restaurante:
        # json.dump(): Função do módulo json que converte um objeto Python (no caso, a lista dados) em uma string JSON e a escreve em um arquivo.
        # dados: A lista de itens do restaurante atual.
        # arquivo_restaurante: O arquivo onde os dados serão escritos.
        # indent=4: Define a indentação do JSON para facilitar a leitura (opcional).
        json.dump(dados, arquivo_restaurante, indent=4)
```

&nbsp;
&nbsp;

### 5 FastAPI

#### 5.1 Usando o FastAPI

Neste capitulo vamos precisar executar o arquivo `app.py`, usado nos capitulos anteriores.

Antes de iniciarmos o uso do FastAPI, foi feito modificacoes para criacao dos arquivos com restaurantes e seus respectivos cardapios.

Versao atualizado do arquivo `app.py`.

```PY
import requests  # Importando a biblioteca requests para realizar requisições HTTP
import json # Importando o modulo json para trabalhar com dados em formato JSON
import os # Importando o módulo os para utilizar a combinacao dos caminhos de forma segura e independente do sistema operacional.

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'  # URL da API que contém os dados dos restaurantes
response = requests.get(url)  # Fazendo uma requisição GET para a URL e armazenando a resposta em 'response'

print(response)  # Imprimindo a resposta completa (para fins de depuração)

if response.status_code == 200:  # Verificando se a requisição foi bem-sucedida (código de status 200)
    dados_json = response.json()  # Convertendo a resposta JSON para um dicionário Python
    dados_restaurante = {}  # Criando um dicionário para armazenar os dados dos restaurantes, organizados por nome
    #print(dados_json)

    # Iterando sobre os dados JSON
    for item in dados_json: 
        nome_do_restaurante = item['Company'] # Obtendo o nome do restaurante a partir do item atual
        #contador += 1

        # Verificando se o restaurante já existe no dicionário
        if nome_do_restaurante not in dados_restaurante:
            # Se não existe, cria uma nova entrada no dicionário
            dados_restaurante[nome_do_restaurante] = []

        # Adiciona um novo item ao restaurante no dicionário
        dados_restaurante[nome_do_restaurante].append({
            "item": item['Item'],
            "price": item['price'],
            "description": item['description']
        })

    print(dados_restaurante)  # Imprimindo o dicionário final com os dados dos restaurantes organizados por nome
else:
    print(f'O erro foi {response.status_code}')  # Imprimindo o código de status do erro caso a requisição falhe

caminho_base = '/home/ernane/Documents/GIT/alura/formacoes/formacoes Python/01. Object Oriented Python/05. Object Orientation and API/fastapi' # Define o diretório base onde os arquivos serão criados.

# Iteração sobre o dicionário: Inicia um loop for para percorrer todas as chaves e valores do dicionário dados_restaurante.
# Desempacotamento: A cada iteração, a chave (nome do restaurante) é atribuída à variável nome_do_restaurante e o valor (lista de itens) é atribuído à variável dados.
for nome_do_restaurante, dados in dados_restaurante.items():

    # os.path.join(): Garante que as barras sejam inseridas corretamente, mesmo em sistemas Windows ou Linux.
    # string formatada (f-string) para o nome do arquivo, usando o nome do restaurante como base e adicionando a extensão .json
    # A variável nome_do_arquivo agora contém o caminho completo, concatenando o caminho_base com o nome do arquivo.
    nome_do_arquivo = os.path.join(caminho_base, f"{nome_do_restaurante}.json") 
    
    # Abre um arquivo para escrita ('w') com o nome gerado anteriormente.
    # Gerenciamento de recursos: O with garante que o arquivo seja fechado corretamente, mesmo que ocorra alguma exceção.
    with open(nome_do_arquivo,'w') as arquivo_restaurante:

        # json.dump(): Função do módulo json que converte um objeto Python (no caso, a lista dados) em uma string JSON e a escreve em um arquivo.
        # dados: A lista de itens do restaurante atual.
        # arquivo_restaurante: O arquivo onde os dados serão escritos.
        # indent=4: Define a indentação do JSON para facilitar a leitura (opcional).
        json.dump(dados, arquivo_restaurante, indent=4)
```

&nbsp;

**Linhas acrescentadas/modificas para o capitulo**

```PY
# ... (resto do código)
import os

# ... (resto do código)
    nome_do_arquivo = os.path.join(caminho_base, f"{nome_do_restaurante}.json")

# ... (resto do código)
```

&nbsp;

**FastAPI**

Link tutorial para instalacao e uso do *FastAPI*

```https://fastapi.tiangolo.com/tutorial/```

&nbsp;

Comando para instalar o *FastAPI*:

```BASH
pip install fastapi
```

Lembrando de ativar o ambiente virtual para instalacao.

&nbsp;

Apos a instalacao, podemos atualizar o arquivo `requirementes.txt` com o mesmo comando usado anteriormente.

```BASH
pip freeze > requirements.txt
```

&nbsp;

Acessar arquivo `requirements.txt` por linha de comando:

```BASH
cat requirements.txt
```

&nbsp;

Criar arquivo `main.py`:

```BASH
touch main.py
```

&nbsp;

Primeiro *endpoint* com `Hello World` no arquivo `main.py`.

```PY
from fastapi import FastAPI

app = FastAPI()

@app.get('/api/hello') # endpoint /api/hello e' local, sendo possivel apenas executar local
def hello_world():
    return {"message": "Hello World"}
```

&nbsp;

Para rodar o *endpoint* localmente, precisamos instalar `uvicorn` e depois executar o comando para rodar o endpoint.

Instalar uvicorn:

```BASH
pip install uvicorn
```

ou

```BASH
sudo apt install uvicorn
```

&nbsp;

```BASH
uvicorn main:app --reload
```

&nbsp;

#### 5.2 Criando e consultando um endpoint

**Criaremos um endpoint para os restaurantes**

```PY
from fastapi import FastAPI, Query  # Importa as classes FastAPI e Query do framework FastAPI
import requests  # Importa a biblioteca requests para fazer requisições HTTP

app = FastAPI()  # Cria uma instância da aplicação FastAPI, que será o ponto de entrada para nossas rotas


@app.get('/')  # Define uma rota GET para a raiz da aplicação (/)
def hello_world():
    """Endpoint que exibe uma mensagem de boas-vindas.

    Retorna:
        dict: Um dicionário com a chave 'message' e o valor 'Hello World'.
    """
    return {'message': 'Hello World'}  # Retorna um JSON com a mensagem de boas-vindas

@app.get('/restaurantes/')  # Define uma rota GET para buscar informações sobre restaurantes
def get_restaurantes(restaurante: str = Query(None)):  # Define um parâmetro opcional 'restaurante' para filtrar por nome
    """Endpoint para buscar informações sobre restaurantes.

    Args:
        restaurante (str, optional): Nome do restaurante a ser buscado. Defaults to None.

    Returns:
        dict: Um dicionário com os dados dos restaurantes encontrados ou uma mensagem de erro.
    """

    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'  # URL da API externa que contém os dados dos restaurantes
    response = requests.get(url)  # Faz uma requisição HTTP GET para a URL e armazena a resposta em 'response'

    if response.status_code == 200:  # Verifica se a requisição foi bem-sucedida (código 200 indica sucesso)
        dados_json = response.json()  # Converte a resposta JSON em um dicionário Python

        if restaurante is None:  # Se nenhum restaurante foi especificado, retorna todos os restaurantes
            return {'Dados': dados_json}  # Retorna todos os dados da API

        dados_restaurante = []  # Cria uma lista vazia para armazenar os dados dos restaurantes encontrados
        for item in dados_json:  # Itera sobre cada item (restaurante) na resposta da API
            if item['Company'] == restaurante:  # Verifica se o nome do restaurante corresponde ao buscado
                # Adiciona as informações do restaurante encontrado à lista
                dados_restaurante.append({
                    "item": item['Item'],
                    "price": item['price'],
                    "description": item['description']
                })

        return {'Restaurante': restaurante, 'Cardapio': dados_restaurante}   
  # Retorna um dicionário com o nome do restaurante e seu cardápio

    else:  # Se a requisição falhou
        return {'Erro': f'{response.status_code} - {response.text}'}  # Retorna um dicionário com uma mensagem de erro indicando o código de status e a mensagem de erro da API
```

&nbsp;

**Explicações Adicionais:**

- **FastAPI:** Um *framework web Python*, rápido e assíncrono, para construir *APIs*.
- **@app.get():** Decorador que define uma rota *HTTP GET*.
- **Query:** Um parâmetro opcional para a rota, permitindo que o usuário forneça um valor para filtrar os resultados.
- **requests:** Uma biblioteca *Python* para fazer requisições *HTTP*.
- **JSON:** Formato de troca de dados leve e fácil de entender, utilizado para transmitir dados entre sistemas.
- **status_code:** Um atributo da resposta *HTTP* que indica o status da requisição (e.g., `200 - OK`, `404 - Not Found`).

&nbsp;

#### Mais sobre FastAPI

**FastAPI**

**O que é FastAPI?**

*FastAPI* é um *framework Python* moderno e de alto desempenho, projetado para criar *APIs* (*Interfaces de Programação de Aplicações*) rapidamente e com facilidade. Ele combina a simplicidade do *Python* com funcionalidades avançadas, tornando-o uma excelente escolha para desenvolver *APIs RESTful* e *GraphQL*.

&nbsp;

**Por que usar FastAPI?**

- **Alta performance:** *FastAPI* é um dos *frameworks Python* mais rápidos disponíveis, rivalizando com frameworks como *Node.js* e *Go*.
- **Facilidade de uso:** Sua sintaxe é intuitiva e baseada em *Python* puro, tornando-o fácil de aprender e usar.
- **Tipo hints:** Utiliza tipo hints para garantir a segurança de tipos e gerar automaticamente documentação interativa.
- **Asyncio:** Suporta programação assíncrona, permitindo lidar com várias requisições simultaneamente.
- **Validação de dados:** Utiliza *Pydantic* para validar automaticamente os dados de entrada e saída das suas *APIs*.
- **Documentação interativa:** Gera automaticamente documentação interativa da sua *API* em formato *OpenAPI* (*Swagger UI*), facilitando o desenvolvimento e o uso da *API*.

&nbsp;

**Conceitos-chave**

- **Rotas:** Definem os endpoints da sua *API*, ou seja, os caminhos que os clientes podem acessar para interagir com a sua aplicação.
- **Métodos HTTP:** Os métodos *HTTP* (*GET*, *POST*, *PUT*, *DELETE*, etc.) indicam o tipo de operação que será realizada na rota.
- **Parâmetros:** Dados que são passados para a função da rota, como parâmetros de caminho, *query parameters* ou dados no corpo da requisição.
- **Respostas:** Os dados que são retornados pela função da rota.
- **Asyncio:** Permite escrever código assíncrono de forma mais concisa e eficiente, utilizando corrotinas.
- **Pydantic:** Biblioteca utilizada pelo *FastAPI* para definir modelos de dados e validar dados de entrada e saída.

&nbsp;

**Exemplo básico**

```PY
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

Neste exemplo, criamos uma aplicação *FastAPI* e definimos uma rota GET para a raiz (`/`). Quando um cliente fizer uma requisição *GET* para essa rota, a função `root` será executada e retornará um *JSON* com a mensagem "`Hello World`".

&nbsp;

**Recursos adicionais**

- **Documentação oficial:** https://fastapi.tiangolo.com/
- **Tutorial completo:** https://kinsta.com/pt/blog/fastapi/

&nbsp;

**Em resumo**

*FastAPI* é uma ferramenta poderosa e versátil para desenvolver *APIs* em *Python*. Sua facilidade de uso, alta performance e recursos avançados o tornam uma excelente escolha para diversos tipos de projetos. Com ela possibilita a busca em construir *APIs* robustas e escaláveis, o *FastAPI* é uma ótima opção.

&nbsp;

**Asyncio e Corrotinas**

**O que é Asyncio?**

*Asyncio* é um módulo nativo do *Python* que permite escrever código assíncrono de forma mais concisa e eficiente. Essa é uma ferramenta poderosa, especialmente quando lidamos com *I/O* (entrada/saída) como requisições de rede, acesso a bancos de dados ou operações de leitura/escrita em arquivos.

&nbsp;

**Mas o que significa "assíncrono"?**

Imagine que você está em um restaurante. Quando você faz um pedido, você não fica parado esperando a comida ser preparada. Em vez disso, você pode conversar com seus amigos enquanto a cozinha prepara o seu pedido. Quando a comida estiver pronta, você será avisado e poderá começar a comer.

No mundo da programação, o *Asyncio* funciona de forma similar. Em vez de esperar que uma operação termine para iniciar a próxima, o programa pode continuar fazendo outras tarefas enquanto a primeira operação está em andamento. Isso permite que o programa seja mais responsivo e eficiente, especialmente quando precisa lidar com várias tarefas ao mesmo tempo.

&nbsp;

**E o que são corrotinas?**

*Corrotinas* são como funções especiais que podem ser suspensas e retomadas em um ponto posterior. Elas são a base da programação assíncrona em *Python*. Quando uma *corrotina* encontra uma operação assíncrona (como uma requisição *HTTP*), ela é suspensa até que a operação seja concluída. Enquanto isso, o programa pode executar outras *corrotinas*.

&nbsp;

**Por que usar Asyncio e Corrotinas?**

- **Melhor desempenho:** Ao permitir que o programa execute várias tarefas ao mesmo tempo, o *Asyncio* pode melhorar significativamente o desempenho em aplicações *I/O-bound*.
- **Código mais conciso:** A sintaxe do *Asyncio*, com as palavras-chave `async` e `await`, torna o código assíncrono mais fácil de escrever e entender.
- **Escalabilidade:** Aplicações assíncronas podem lidar com um grande número de conexões simultâneas de forma mais eficiente.

&nbsp;

**Exemplo:**

```PY
import asyncio

async def fetch_data():
    # Simula uma operação assíncrona (por exemplo, uma requisição HTTP)
    await asyncio.sleep(2)
    return {'data': 'Algumas informações'}

async def main():
    task = asyncio.create_task(fetch_data())
    print('Fazendo outras coisas...')
    result = await task
    print(result)

asyncio.run(main())
```

Neste exemplo, a função `fetch_data` simula uma operação assíncrona que leva 2 segundos para ser concluída. A função `main` cria uma tarefa para executar `fetch_data` e, enquanto a tarefa está em andamento, imprime uma mensagem. Quando a tarefa for concluída, o resultado é impresso.

&nbsp;

**Em resumo:**

- **Asyncio:** Um módulo *Python* para programação assíncrona.
- **Corrotinas:** Funções especiais que podem ser suspensas e retomadas.
- **Benefícios:** Melhor desempenho, código mais conciso e escalabilidade.

&nbsp;

**Em relação ao FastAPI:**

O *FastAPI* utiliza o *Asyncio* para permitir que suas *APIs* sejam altamente performantes e capazes de lidar com um grande número de requisições simultâneas. Ao usar o *FastAPI*, você pode criar *APIs* assíncronas de forma fácil e intuitiva, sem se preocupar com os detalhes da implementação do *Asyncio*.

&nbsp;

**Asyncio e FastAPI: Uma Integração Natural**

O *FastAPI* já vem com o *Asyncio* integrado por padrão! Isso significa que você não precisa se preocupar em importar o módulo *asyncio* explicitamente na maioria dos casos.

&nbsp;

**Por que o Asyncio é Tão Importante no FastAPI?**

- **Alta Concorrência:** O *Asyncio* permite que o *FastAPI* manipule múltiplas requisições simultaneamente de forma eficiente, sem bloquear o processo principal. Isso é crucial para construir *APIs* escaláveis e responsivas.
- **I/O Bound Operations:** Muitas operações em *APIs*, como acesso a bancos de dados ou chamadas para outras *APIs*, são *I/O bound*. O *Asyncio* permite que o processador trabalhe em outras tarefas enquanto aguarda a conclusão dessas operações.
- **Simplicidade:** O *FastAPI* abstrai muitos dos detalhes do *Asyncio*, tornando mais fácil para você escrever código assíncrono sem se preocupar com os detalhes técnicos.

&nbsp;

**Como Usar o Asyncio no FastAPI?**

- **Funções Assíncronas:** Defina suas funções de rota como `async def` para torná-las assíncronas.
- **Await:** Utilize a palavra-chave `await` para esperar que uma operação assíncrona seja concluída.

&nbsp;

**Exemplo**

```PY
from fastapi import FastAPI
import time

app = FastAPI()

async def slow_task():
    await asyncio.sleep(2)
    return {"message": "Task completed"}

@app.get("/")
async def root():
    task = asyncio.create_task(slow_task())
    return {"message": "Starting a slow task"}
```

&nbsp;

**O que acontece neste exemplo:**

1. A função `slow_task` simula uma operação assíncrona que leva 2 segundos para ser concluída.
2. A rota `/` inicia a tarefa `slow_task` e retorna uma mensagem indicando que a tarefa foi iniciada.
3. Enquanto a tarefa está sendo executada, o *FastAPI* pode atender a outras requisições.

&nbsp;

**Em resumo**

O *FastAPI* e o *Asyncio* trabalham em conjunto para fornecer uma experiência de desenvolvimento de *APIs* eficiente e escalável. Ao utilizar o *Asyncio*, você pode criar *APIs* que respondem rapidamente a um grande número de requisições, tornando suas aplicações mais robustas e performantes.

&nbsp;

**Pontos-chave a lembrar**

- **Integração:** O *Asyncio* está integrado ao *FastAPI* por padrão.
- **Funções Assíncronas:** Use `async def` para definir funções assíncronas.
- **Await:** Utilize `await` para esperar que uma operação assíncrona seja concluída.
- **Benefícios:** Melhora o desempenho, permite lidar com múltiplas requisições simultaneamente e torna o código mais conciso.