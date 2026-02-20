"""
POO - Classes

Em POO, Classes nada mais são do que modelos dos objetos do mundo real sendo representados
computacionalmente

Imagine que você queira fazer um sistema para automatizar o controle das lâmpadas da sua casa

Classes podem conter:
    - Atributos -> Representam as características do objeto. Ou seja, pelos atributos
                   conseguimos representar computacionalmente os estados de um objeto.
                   No caso da lâmpada, possívelmente iríamos querer saber se a lâmpada
                   é 110 ou 220 volts, qual a cor da sua luz, qual é a luminosidade e etc.

    - Métodos (funções) -> Representam os comportamentos do objeto. Ou seja, as ações que
                           este objeto pode realizar no seu sistema. No caso da lâmpada,
                           por exemplo, um comportamento comum que muito provavelmente
                           iríamos querer representar no nosso sistema é o de ligar e
                           desligar a mesma.

Em Python, para definir uma classe utilizamos a palavra reservada "class".

OBS: Utilizamos a palavra "pass" em Python quando temos um bloco de código que ainda não
está implementado

OBS: Quando nomeamos nossas classes em Python, utilizamos por convenção o nome com inicial
em maiúscula. Se o nome for composto, utiliza-se as iniciais de cada palavra em maiúsculo,
todas juntas

OBS: Quando estamos planejando um software e definimos quais classes teremos que ter no
sistema, chamamos estes objetos que serão mapeados para classes de "entidade"

Dica: Em computação não utilizamos: acentuação, caracteres especiais, espaços ou similares para
nomes de classes, atributos, métodos, arquivos, pastas e etc.

class Lampada:
    pass


class ContaCorrente:
    pass


class Produto:
    pass


class Usuario:
    pass


class Int:
    pass


valor = int("42")  # Casting
print(help(int))
inteiro = Int()
print(type(inteiro))
"""

# ====================

"""
POO - Atributos

Atributos -> Representam as características do objeto. Ou seja, pelos atributos nós conseguimos
representar computacionalmente os estados de um objeto.

Em Python, dividimos os atributos em 3 grupos:
    - Atributos de Instância
    - Atributos de Classe
    - Atributos Dinâmicos

# Atributos de instância: São atributos declarados dentro do método construtor

# OBS: Método construtor: É um método especial utilizado para a construção do objeto

# Em Java, uma classe Lâmpada, incluindo seus atributos ficaria mais ou menos:

public class Lampada() {
    private int voltagem;
    public String cor;
    protected Boolean ligada = false;

    public Lampada(int voltagem, String cor) {
        this.voltagem = voltagem;
        this.cor = cor;
    }

    public int getVoltagem() {
        return this.voltagem;
    }
}

Em Python, por convenção, ficou estabelecido que, todo atributo de uma classe é publico.
Ou seja, pode ser acessado em todo o projeto. Caso queiramos demonstrar que determinado
atributo deve ser tratado como private, ou seja, que deve ser acessado/utilizado somente
dentro da própria classe onde está declarado, utiliza-se __ duplo underscore no início de
seu nome. Isso é conhecido como Name Mangling

# OBS: Lembre-se que isso é apenas uma convenção, ou seja, a linguagem Python não vai
# impedir que façamos acesso aos atributos "privados" fora da classe

# Exemplo
user = Acesso('user@gmail.com', '123456')
print(user.email)
print(user.__senha)  # AttributeError
print(user._Acesso__senha)  # Temos acesso. Mas, não deveríamos fazer este acesso.

user.mostra_email()
user.mostra_senha()

# O que significa atributos de instância?
# Significa que ao criarmos instâncias/objetos de uma classe, todas as instâncias
# terão estes atributos

user1 = Acesso('user1@gmail.com', '123456')
user2 = Acesso('user2@gmail.com', '654321')

user1.mostra_email()
user2.mostra_email()

# Atributos de Classe

# Atributos de classe são atributos declarados diretamente na classe, ou seja,
# fora do construtor. Geralmente já inicializamos um valor, e este valor é
# compartilhado entre todas as instâncias da classe. Ou seja, ao invés de cada
# instância da classe ter seus próprios valores como é o caso dos atributos
# de instância, com os atributos de classe, todas as instâncias terão o mesmo
# valor para este atributo

produto1 = Produto('PlayStation 5', 'Video Game', 499)
produto2 = Produto('Xbox Series X', 'Video Game', 399)

print(produto1.valor)  # Acesso possível, mas incorreto de um atributo de classe
print(produto2.valor)  # Acesso possível, mas incorreto de um atributo de classe

# OBS: Não precisamos criar uma instância de uma classe para fazer acesso a um atributo
# de classe

print(Produto.imposto)  # Acesso correto de um atributo de classe

print(p1.id)
print(p2.id)

# OBS: Em linguagens como o Java, os atributos conhecidos como atributos de classe aqui em
# Python são chamados de atributos estáticos

# Classes com Atributo de Instância Público


class Lampada:
    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo
        self.ativo = True


class Produto:
    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

# Atributos Públicos e Atributos Privados

class Acesso:
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_email(self):
        return self.email

    def mostra_senha(self):
        return self.__senha


acesso = Acesso("joao@gmail.com", "1234")
print(acesso.email)
print(acesso.mostra_senha())

# Refatorar a classe Produto

class Produto:
    # Atributos de classe
    imposto = 1.05  # 0.05%
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = valor * Produto.imposto
        Produto.contador = self.id


# Atributos Dinâmicos -> Um atributo de instância que pode ser criado em tempo de execução
# OBS: Será exclusiva da instância que o criou

p1 = Produto("iPhone 17", "Celular", 900)
p2 = Produto("MacBook", "Notebook", 1000)
print(p1.id, end=" ")
print(p1.valor)

print(p2.id, end=" ")
print(p2.valor)

# Criando um atributo dinâmico em tempo de execução
p2.peso = "5kg"  # Note que na classe Produto não existe o atributo peso

# print(f"Produto: {p1.nome}, Descrição: {p1.descricao}, Valor: {p1.valor}, Peso: {p1.peso}")

print(
    f"Produto: {p2.nome}, Descrição: {p2.descricao}, Valor: {p2.valor}, Peso: {p2.peso}"
)

# Deletando atributos
print(p1.__dict__)
print(p2.__dict__)

del p2.descricao
del p2.valor

print("\n=============\n")

print(p1.__dict__)
print(p2.__dict__)
"""

# ====================

"""
POO - Métodos

- Métodos (funções) -> Representam os comprtamentos do objeto. Ou seja, as ações que
este objeto pode realizar no seu sistema

Em Python, dividimos os métodos em 2 grupos: Métodos de instância e Métodos de Classe

# Métodos de Instância

# O método dunder init (__init__) é um método especial chamado de construtor e sua função
é construir o objeto a partir da classe

# OBS: Todo elemento em Python que inicia a finaliza com duplo underscore é chamado de dunder
(Double Underscore)

# OBS: Os métodos/funções dunder em Python são chamados de "Métodos Mágicos"

ATENÇÃO! Por mais que possamos criar nossas próprias funções utilizando dunder, não é aconselhado. Python
possui vários métodos com esta forma de nomenclatura e pode ser que mudemos o comportamento dessas funções mágicas
internas da linguagem. Então, evite ao máximo. De preferência nunca o faça.

# Métodos são escritos em letras minúsculas. Se o nome for composto, o nome terá as palavras separadas por
# underscore

class Produto:
    imposto = 1.05

    def __init__(self, nome, valor, quantidade):
        self.__nome = nome
        self.__valor = valor
        self.__quantidade = quantidade

    def get_nome(self):
        return self.__nome

    def get_valor(self):
        return self.__valor

    def get_quantidade(self):
        return self.__quantidade

    def calcula_total(self):
        return (self.__valor * self.__quantidade) * Produto.imposto


produto1 = Produto("Café", 4, 4)
print(produto1.get_nome(), produto1.get_valor(), produto1.get_quantidade())
print(produto1.calcula_total())
"""

# ====================

"""
POO - Objetos

Objetos -> São instâncias da classe. Ou seja, após o mapeamento do objeto do mundo real para a sua representação
computacional, devemos poder criar quantos objetos forem necessários. Podemos pensar nos objetos/instâncias de uma
classe como variáveis do tipo definido na classe

class Lampada:
    def __init__(self, cor, voltagem, preco):
        self.cor = cor
        self.voltagem = voltagem
        self.preco = preco
        self.ligado = False

    def ligar_desligar(self):
        if self.ligado:
            self.ligado = False
        else:
            self.ligado = True
        return self.ligado


# Instâncias / Objetos
lampada1 = Lampada("Branca", 110, 60)
print(lampada1.ligar_desligar())
print(lampada1.ligar_desligar())
print(lampada1.ligar_desligar())

class ContaCorrente:
    def __init__(self, id, nome, saldo):
        self.id = id
        self.nome = nome
        self.saldo = saldo

    def get_info(self):
        return f"{self.id} - {self.nome}: ${self.saldo}"


conta_corrente1 = ContaCorrente(1, "João", 400_000)
conta_corrente2 = ContaCorrente(2, "Paula", 4_000_000)

print(conta_corrente1.get_info())
print(conta_corrente2.get_info())
"""

# ====================

"""
POO - Abtração e Encapsulamento

O grande objetivo da POO é encapsular nosso código dentro de um grupo lógico e hierárquico utilizando clases

Encapsular -> cápsula

             classe
-------------------------------
|     atributos e métodos     |
-------------------------------

# Relembrando Atributos / Métodos privados em Python

Imagina que temos uma classe chamada Pessoa, contendo um atributo privado chamado __nome e outro método
privado chamado __falar()

Esses elementos privados só devem/deveriam ser acessados dentro da classe. Mas, Python não bloqueia este
acesso fora da classe. Com Python acontece um fenômeno chamado Name Mangling, que faz uma alteração na
forma de se acessar os elementos privados, conforme:

_Classe__elemento

Exemplo - Acessando elementos privados fora da classe:
instancia._Pessoa__nome
instacia._Pesosa__falar()

Abstração em POO, é o ato de expor apenas dados relevantes de uma classe, escondendo atributos e métodos
privados de usuário.

from __future__ import annotations


class Conta:
    contador: int = 400

    def __init__(self, titular: str, saldo: float, limite: float) -> None:
        self.__numero: int = Conta.contador
        self.__titular: str = titular
        self.__saldo: float = saldo
        self.__limite: float = limite
        Conta.contador = self.__numero + 1

    def extrato(self) -> None:
        print(
            f"Saldo de: ${self.__saldo:.2f} do titular {self.__titular} com limite de ${self.__limite:.2f}"
        )

    def depositar(self, valor: float) -> None:
        if valor > 0:
            self.__saldo += valor
        else:
            print("O valor deve ser positivo")

    def sacar(self, valor: float) -> None:
        if valor > 0:
            if valor <= self.__saldo:
                self.__saldo -= valor
            else:
                print("Saldo insuficiente!")
        else:
            print("O valor deve ser positivo")

    def transferir(self, valor: float, conta_destino: Conta) -> None:
        if valor > 0:
            if valor <= self.__saldo:
                # 1 - Remover o valor da conta de origem
                self.__saldo -= valor

                # 2 - Adicionar o valor na conta de destino
                conta_destino.__saldo += valor
            else:
                print("Saldo insuficiente!")
        else:
            print("O valor deve ser positivo")


# Testando
print("\n\n======== EXTRATO ========")
conta1 = Conta("João", 150.00, 1500.00)
conta1.extrato()

conta2 = Conta("Paula", 300.00, 2000.00)
conta2.extrato()

print("\n\n======== TRANSFERIR ========")
conta2.transferir(65, conta1)

conta1.extrato()
conta2.extrato()

print("\n\n======== SACAR ========")
conta1.sacar(15)
conta1.extrato()

print("\n\n======== DEPOSITAR ========")
conta1.depositar(150)
conta1.extrato()
"""
