"""
POO - Herança (Inheritance)

A ideia de herança é o de reaproveitar código. Também extender nossas classes.

OBS: Com a herança, a partir de uma classe existente, nós extendemos outra classe que passa a herdar
atributos e métodos da classe herdada.

Cliente
    - nome
    - sobrenome
    - cpf
    - renda

Funcionario
    - nome
    - sobrenome
    - cpf
    - matricula

Pergunta: Existe alguma entidade genérica o suficiente para encapsular os atributos e métodos comuns a outras
entidades?

class Cliente:
    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"


class Funcionario:
    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"


cliente1 = Cliente("João", "Victor", "123.456.789-00", 5000)
funcionario1 = Funcionario("John", "Doe", "987.654.321-00", 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())

OBS: Quando uma classe herda de outra classe, ela herda TODOS os atributos e métodas da classe herdada.

Quando uma classe herda de outra classe, a classe é conhecida por:

[Pessoa]
- Super Classe
- Classe Mãe
- Classe Pai
- Classe Base
- Classe Genérica

Quando uma classe herda de outra classe, ela é chamada de:

[Cliente, Funcionario]
- Sub Classe
- Classe Filha
- Classe Específica

class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"


class Cliente(Pessoa):
    # Cliente herda de Pessoa

    def __init__(self, nome, sobrenome, cpf, renda):
        Pessoa.__init__(
            self, nome, sobrenome, cpf
        )  # Forma não comum de acessar dados da classe mãe
        self.__renda = renda


class Funcionario(Pessoa):
    # Funcionario herda de Pessoa

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(
            nome, sobrenome, cpf
        )  # Forma mais comum de acesar dados da classe mãe
        self.__matricula = matricula


cliente1 = Cliente("João", "Victor", "123.456.789-00", 5000)
funcionario1 = Funcionario("John", "Doe", "987.654.321-00", 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())

print('\n==================\n')

print(cliente1.__dict__)
print(funcionario1.__dict__)

# Sobreescrita de Métodos (Overriding)

Sobreescrita de método é quando reescrevemos/reimplementamos um método presente na super classe em uma classe
ou em sub classes

class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"


class Cliente(Pessoa):
    # Cliente herda de Pessoa

    def __init__(self, nome, sobrenome, cpf, renda):
        Pessoa.__init__(
            self, nome, sobrenome, cpf
        )  # Forma não comum de acessar dados da classe mãe
        self.__renda = renda

    def nome_completo(self):
        return f"Cliente: {self._Pessoa__nome} {self._Pessoa__sobrenome} - Renda: {self.__renda}"


class Funcionario(Pessoa):
    # Funcionario herda de Pessoa

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(
            nome, sobrenome, cpf
        )  # Forma mais comum de acesar dados da classe mãe
        self.__matricula = matricula

    def nome_completo(self):
        return f"Funcionário: {self._Pessoa__nome} - Matrícula: {self.__matricula}"


cliente1 = Cliente("João", "Victor", "123.456.789-00", 5000)
print(cliente1.nome_completo())

funcionario1 = Funcionario("John", "Doe", "987.654.321-00", 1234)
print(funcionario1.nome_completo())
"""

# =================

"""
POO - Propriedades

Em linguagens de programação como o Java, ao declararmos atributos privados nas classes,
costumamos criar métodos públicos para manipulação desses atributos. Esses métodos são
conhecidos por "getters" e "setters", onde os getters retornam o valor do atributo e os
setters alteram o valor do mesmo

class Conta:
    # Atributos de classe
    contador = 0

    def __init__(self, titular, saldo, limite):
        # Atributos de instância
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        return f"Saldo: ${self.__saldo:.2f} do cliente {self.__titular}"

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destinatario):
        self.__saldo -= valor
        destinatario.__saldo += valor

    def get_titular(self):
        return self.__titular

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite


conta1 = Conta(titular="João", saldo=200.00, limite=500)
conta2 = Conta(titular="Paula", saldo=100.00, limite=300)

print("\n====== EXTRATO ======")
print(conta1.extrato())
print(conta2.extrato())

print("\n====== GETTERS ======")
print(conta1.get_titular())
print(conta1.get_saldo())
print(conta1.get_limite())

print("\n====== SETTERS ======")
print(conta1.get_limite())
conta1.set_limite(limite=1200)
print(conta1.get_limite())

class Conta:
    # Atributos de classe
    contador = 0

    def __init__(self, titular, saldo, limite):
        # Atributos de instância
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @property
    def valor_total(self):
        return self.__saldo + self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    def extrato(self):
        return f"Saldo: ${self.__saldo:.2f} do cliente {self.__titular}"

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destinatario):
        self.__saldo -= valor
        destinatario.__saldo += valor


conta1 = Conta(titular="João", saldo=200.00, limite=500)
conta2 = Conta(titular="Paula", saldo=100.00, limite=300)

print(conta1.extrato())
print(conta2.extrato())

soma = conta1.saldo + conta2.saldo
print(f"A soma do saldo das contas é {soma}")

print(conta1.__dict__)
conta1.limite = 99999
print(conta1.__dict__)
print(conta1.limite)

print(conta1.valor_total)
print(conta2.valor_total)
"""

# =================

"""
POO - O método super()

O método super() se refere à classe mãe:

class Animal:
    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def faz_som(self, som):
        print(f"O {self.__nome} fala {som}")

class Gato(Animal):
    def __init__(self, nome, especie, raca):
        super().__init__(nome, especie)
        super().faz_som("au au au au")
        self.__raca = raca


tom = Gato("Tom", "Felino", "Bosques da Noruega")
tom.faz_som("miau")
"""

# =================

"""
POO - Heranças Múltiplas

Heranças Múltiplas nada mais é do que a possibilidade de uma classe herdar de múltiplas classes, fazendo com que a
classe filha herde todos os atributos e métodos de todas as classes herdadas

# OBS: A Herança Múltipla pode ser feita de duas maneiras:
#   - Por Multiderivação Direta
#   - Por Multiderivação Indireta

# Exemplo 1 - Multiderivação Direta
class Base1:
    pass


class Base2:
    pass


class Base3:
    pass


class MultiDerivada(Base1, Base2, Base3):
    pass


# Exemplo 2 - Multiderivação Indireta
class Base1:
    pass


class Base2(Base1):
    pass


class Base3(Base2):
    pass


class MultiDerivada(Base3):
    pass


# OBS: Não importa se a derivação é direta ou indireta. A classe que realizar a herança herdará todos os atributos
# e métodos das super classes.

class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f"Eu sou o {self.__nome}"


class Aquatico(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f"{self._Animal__nome} está nadando."

    def cumprimentar(self):
        return f"Eu sou o {self._Animal__nome} do mar!"


class Terrestre(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f"{self._Animal__nome} está andando."

    def cumprimentar(self):
        return f"Eu sou o {self._Animal__nome} da terra!"


class Pinguim(Aquatico, Terrestre):
    def __init__(self, nome):
        super().__init__(nome)


baleia = Aquatico("Wally")
print(baleia.nadar())
print(baleia.cumprimentar())

print("\n===========")

tatu = Terrestre("Xim")
print(tatu.andar())
print(tatu.cumprimentar())

print("\n===========")

pinguim = Pinguim("Tux")
print(pinguim.andar())
print(pinguim.nadar())
print(pinguim.cumprimentar())
"""

# =================

"""
POO - MRO - Method Resolution Order

Method Resolution Order (Ordem de Resolução de Métodos), é a ordem de execução dos métodos (quem será executado primeiro)

Em Python, a gente pode conferir a ordem de execução dos métodos (MRO) de 3 formas:
    - Via propriedade da classe __mro__
    - Via método mro()
    - Via help

class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f"Eu sou o {self.__nome}"


class Aquatico(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f"{self._Animal__nome} está nadando."

    def cumprimentar(self):
        return f"Eu sou o {self._Animal__nome} do mar!"


class Terrestre(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f"{self._Animal__nome} está andando."

    def cumprimentar(self):
        return f"Eu sou o {self._Animal__nome} da terra!"


class Pinguim(Aquatico, Terrestre):
    def __init__(self, nome):
        super().__init__(nome)


pinguim = Pinguim("Tux")
print(pinguim.cumprimentar())
print(Pinguim.__mro__)
print(Pinguim.mro())
print(help(Pinguim))
"""

# =================

"""
POO - Polimorfismo

Poli -> Muitas
Morfis -> Formas

quando reimplementamos um método presente na classe pai em classes filhas, estamos realizando
uam sobrescrita de método (Overriding)

O overriding é a melhor representação do polimorfismo

class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError("A classe filha precisa implementar este método!")

    def comer(self):
        print(f"{self.__nome} está comendo...")


class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):git
        print(f"{self._Animal__nome} fala au au!")


class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f"{self._Animal__nome} fala miau!")


class Rato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f"{self._Animal__nome} fala algo...")


# animal = Animal('Jonata')
# animal.falar()  # NotImplementedError

cachorro = Cachorro("Rex")
cachorro.falar()

gato = Gato("Shizo")
gato.falar()

rato = Rato("Ratatouille")
rato.falar()
"""

# =================

"""
POO - Métodos Mágicos

Métodos Mágicos, são todos os métodos que utilizam dunder

dunder init -> __init__()
def __init__(self, titulo, autor, paginas)
    self.__titulo = titulo
    self.__autor = autor
    self.__paginas = paginas

dunder repr -> Representação do objeto
def __repr__(self):
    return f'{self.__titulo} escrito por {self.__autor}'

Dunder -> Double Underscore

class Livro:
    def __init__(self, titulo, autor, paginas):
        self.__titulo = titulo
        self.__autor = autor
        self.__paginas = paginas

    def __repr__(self):
        return f"{self.__titulo} escrito por {self.__autor}. Total de {self.__paginas} páginas"

    def __str__(self):
        return self.__titulo

    def __len__(self):
        return self.__paginas

    def __add__(self, outro):
        return self.__paginas + outro.__paginas

    def checar_estoque(): ...

    def checar_fornecedor(): ...


livro1 = Livro("The Language of God", "Francis Collins", 318)
livro2 = Livro("Darwin's God", "Kenneth R. Miller", 215)

print(repr(livro1))
print(livro2)

print(len(livro1), len(livro2))

print(livro1 + livro2)
"""
