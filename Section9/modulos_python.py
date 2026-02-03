"""
Módulo Random e o que são módulos?

- Em Python, módulos nada mais são do que outros arquivos Python

Módulo Random -> Possui várias funções para geração de números pseudo-aleatórios

# OBS: Existem duas formas de se utilizar um módulo ou função

# Forma 1 - Importando o módulo inteiro
import random

# random() -> Gera um número real pseudo-aleatório entre 0 e 1

# OBS: Ao realizar o import inteiro do módulo todas as funções, atributos, classes e propriedades
# que estiverem dentro do módulo ficarão disponíveis (ficarão em memória). Caso você saiba que funções
# você precisa utilizar deste módulo, então esta não seria a forma ideal de utilização. Nós veremos
# uma forma melhor na Forma 2

print(random.random())

# Veja que para utilizar a função random() do pacote random, nós colocamos o nome do pacote e o nome
# da função, separados por ponto

# OBS: Não confunda a função random() com o pacote random. Pode parecer confuso, mas a função random()
# é apenas uma função dentro do módulo random

# Forma 2 - Importando uma função específica do módulo (Forma Recomendada)
from random import random, uniform

# No import acima, estamos falando: Do módulo random, importa a função random()
for i in range(10):
    print(random())

print("================")

# uniform() -> Gera um número real pseudo-aleatório entre os valores estabelecidos
for i in range(10):
    print(uniform(5, 10)) # 10 não é incluído

# randint() -> Gera valores pseudo-aleatórios entre os valores estabelecidos
from random import randint

# Gerador de apostas para MegaSena
for i in range(6):
    print(randint(1, 61), end=" ")  # Começa em 1 e vai até 61

# choice() -> Mostra um valor aleatório entre um iterável
from random import choice

print(choice("Estou aprendendo em Python"))
print(choice([1, 5, 7, 9]))

from random import shuffle

# shuffle() -> Tem a função de embaralhar dados

deck = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7']
print(deck)
shuffle(deck)
print(deck)
"""

# =============

"""
Trabalhando com Módulos Built-in (módulos integrados, que já vem instalados no Python)

# Utilizando alias (apelidos) para módulos/funções
import random as rdm

print(rdm.random())

# Podemos importar todas as funções de um módulo utilizando o *
from random import *

print(random())

# Importando todo o módulo
import random

print(random.random())

# Utilizando alias (apelidos) para módulos/funções
from random import randint as rdi

print(rdi(5, 89))

# Utilizando alias (apelidos) para módulos/funções
from random import randint as rdi, random as rdm, shuffle as shf

print(rdi(5, 89))
print(rdm())

# Costumamos utilizar tuple par colocar múltiplos imports de um mesmo módulo
from random import (choice, randint, random, shuffle)

print(random())
print(randint(3, 7))
lista = ["Teste1", "Teste2", "Teste3"]
shuffle(lista)
print(lista)
print(choice("Escolha uma letra aleatória"))
"""

# =============

"""
Módulos Customizados

Como módulos em Python nada mais são do que arquivos Python, então TODOS os arquivos que criamos
neste curso são módulos Python prontos para serem utilizados

# Importando uma função específica do nosso módulo
from meu_modulo import soma, subtrair

print(soma(5, 3))
print(subtrair(5, 3))

# Importando todo o módulo (Temos acesso a TODOS os elementos do módulo)
import meu_modulo

print(meu_modulo.soma(5, 4))
print(meu_modulo.subtrair(5, 4))

print(meu_modulo.lista_de_usuarios)
print(meu_modulo.coordenadas)
"""

# =============

"""
Módulos Externos

Utilizando o gerenciador de pacotes Python chamado PIP - Python Installer Package

Você pode conhecer todos os pacotes externos oficiais em: https://pypi.org

colorama -> É utilizado para permitir a impressão de textos coloridos no terminal

# Para criar um ambiente virtual, primeiro entramos na pasta do projeto e executamos no terminal:
python -m venv nome-do-ambiente-virtual

# Instalando um módulo:
pip install nome-do-modulo

# Utilizando o pacote colorama
from colorama import Fore, init

init()

print(Fore.BLUE + "Meu nome é João")
print(Fore.MAGENTA + "Meu nome é Paula")
print(Fore.RESET + '[' + Fore.GREEN + 'INFO' + Fore.RESET + '] Sucesso ao iniciar o banco de dados')
print(Fore.RESET + '[' + Fore.RED + 'ERRO' + Fore.RESET + '] Erro ao fazer a conexão')

import pydf

pdf = pydf.generate_pdf("<h1>This is HTML</h1>")

with open("test_doc.pdf", "wb") as file:
    file.write(pdf)
"""

# =============

"""
Pacotes

Módulo -> É apenas um arquivo Python que pode ter diversas funções para utilizarmos

Pacote -> É um diretório contendo uma coleção de módulos

Framework -> Um framework é algo maior: ele define como sua aplicação deve ser construída

OBS: Nas versões 2.x do Python, um pacote Python deveria conter dentro dele um arquivo chamado __init__.py. Nas versões
do Python 3.x, não é mais obrigatório a utilização desse arquivo, mas normalmente ainda é utilizado para manter
compatibilidade

from primeiroPacote import primeiro_pacote_1, primeiro_pacote_2
from segundoPacote.segundo_pacote_1 import soma, subtracao
from segundoPacote.segundo_pacote_2 import pi

print(soma(2, 2))
print(subtracao(3, 1))
print(pi)
"""

# =============

"""
Dunder Name e Dunder Main

Dunder -> Double Underscore

Dunder Name -> __name__

Dunder Main -> __main__

Em Python, são utilizados dunder para criar funções, atributos/propriedades e etc utilizando
Double Underscore para não gerar complito com os nomes desses elementos na programação

# Na linguagem C, temos um programa da seguinte forma:
int main() {
    return 0;
}

# Na linguagem Java, temos um programa da seguinte forma:
public static void main(String[] args) {

}

# Em Python, se executarmos um módulo Python diretamente na linha de comando, internamente
# o Python atribuirá à variável __name__ o valor __main__ indicando que este módulo é o
# módulo de execução principal

Main -> Significa principal

import meu_modulo
from primeiroPacote import primeiro_pacote_1, primeiro_pacote_2
from segundoPacote import segundo_pacote_1, segundo_pacote_2

print("Este é o arquivo principal")
"""
