"""
Lendo arquivos CSV

CSV - Comma Separated Values - Valores Separados por Vírgula

# Separador por vírgula
1, 2, 3, 4, 5, 6
"python", "ciência", "dados", "análise"

# Sepadores por ponto e vírgula
1; 2; 3; 4; 5; 6
"python"; "ciência"; "dados"; "análise"

# Sepadores por espaço
1 2 3 4 5 6
"python" "ciência" "dados" "análise"

# Link útil:
http://dados.gov.br/dataset

# 1. Possível de se trabalhar, mas não é o ideal (trabalhoso)
with open("car-sales.csv", encoding="UTF-8") as arquivo:
    dados = arquivo.read()
    # print(type(dados))
    dados = dados.split(",")[2:]
    print(dados)


# A linguagem Python possui duas formas diferentes de ler dados em arquivos CSV:
#   - Reader -> Permite que iteremos sobre as linhas do arquivo CSV como listas
#   - DictReader -> Permite que iteremos sobre as linhas do arquivo CSV como Ordered Dicts

# Reader
from csv import reader

with open("car-sales.csv", encoding="UTF-8") as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv)  # Pular cabeçalho
    for linha in leitor_csv:
        # Cada linha é uma lista
        print(linha[0])

print("\n\n")

# DictReader
from csv import DictReader

with open("car-sales.csv", encoding="UTF-8") as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        # Cada linha é um Ordered Dict
        print(linha['Make'])
"""

# ======================

"""
Escrevendo em arquivos CSV

reader() (leitor), writer() (escritor)

writerow() -> Escreve uma linha

# writer() -> Gera um objeto para que possamos escrever em um arquivo CSV. Utilizamos o método
# writerow() para escrever cada linha. Este método recebe uma lista

from csv import writer

with open("car-sales2.csv", "a", encoding="UTF-8", newline="") as arquivo:
    escritor_csv = writer(arquivo)
    continuar = None
    # escritor_csv.writerow(["Make", "Colour", "Odometer (KM)", "Doors", "Price"])
    while continuar != "sair":
        continuar = input('Se desejar sair, digite "sair": ')
        if continuar != "sair":
            marca = input("Informe a marca do veículo: ")
            cor = input("Informe a cor do veículo: ")
            kilometragem = input("Informe a kilometragem do veículo: ")
            portas = input("Informe o número de portas do veículo: ")
            preco = input("Informe o preço do veículo: ")
            escritor_csv.writerow([marca, cor, kilometragem, portas, preco])

# DictWriter

# OBS: As chaves dos dicionários devem ser as mesmas utilizadas no cabeçalho

from csv import DictWriter

with open("car-sales2.csv", "a", encoding="UTF-8", newline="") as arquivo:
    cabecalho = ["Make", "Colour", "Odometer (KM)", "Doors", "Price"]
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    continuar = None
    while continuar != "sair":
        continuar = input('Se desejar sair, digite "sair": ')
        if continuar != "sair":
            marca = input("Informe a marca do veículo: ")
            cor = input("Informe a cor do veículo: ")
            kilometragem = input("Informe a kilometragem do veículo: ")
            portas = input("Informe o número de portas do veículo: ")
            preco = input("Informe o preço do veículo: ")
            escritor_csv.writerow(
                {
                    "Make": marca,
                    "Colour": cor,
                    "Odometer (KM)": kilometragem,
                    "Doors": portas,
                    "Price": preco,
                }
            )
"""

# ======================

"""
Conhecendo o Pickle

A função do Pickle é realizar o seguinte processo:

Objeto Python -> Binarização
Binarização -> Objeto Python

Este processo é chamado de serialização/deserialização

# OBS: O módulo Pickle não é seguro contra dados maliciosos e desta forma não é recomendado
# trabalhar com arquivos Pickle vindo de outras pessoas que você não conheça ou de fontes
# desconhecidas

class Animal:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def comer(self):
        print(f"{self.__nome} está comendo...")


class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def mia(self):
        print(f"{self.nome} está miando...")


class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def late(self):
        print(f"{self.nome} está latindo...")


felix = Gato("Felix")
pluto = Cachorro("Pluto")

import pickle

# Fazendo a escrita de arquivos
with open("animais.pickle", "wb") as arquivo:
    pickle.dump((felix, pluto), arquivo)

# Fazendo a leitura de dados em arquivos Pickle
with open("animais.pickle", "rb") as arquivo:
    gato, cachorro = pickle.load(arquivo)
    print(f"O gato chama-se {gato.nome}")
    gato.mia()
    print(f"O tipo do gato é {type(gato)}")

    print("\n")

    print(f"O cachorro chama-se {cachorro.nome}")
    cachorro.late()
    print(f"O tipo do cachorro é {type(cachorro)}")

"""

# ======================

"""
JSON e Pickle

JSON -> JavaScript Object Notation

API -> São meios de comunicação entre os serviços oferecidos por empresas
(Twitter, Facebook, Youtube...) e terceiros (nós desenvolvedores)

import json

ret = json.dumps(["produto", {"PlayStation 5": ("2TB", "Novo", "220V", 2340)}])
print(type(ret))
print(ret)

class Gato:
    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


felix = Gato("Felix", "Vira-lata")
print(felix.__dict__)

ret = json.dumps(felix.__dict__)
print(ret)

# Integrando o JSON com o Pickle
# pip install jsonpickle

import jsonpickle

felix = Gato("Felix", "Vira-lata")
ret = jsonpickle.encode(felix)
print(ret)

# Escrevendo o arquivo JSON/Pickle
with open("felix.json", "w") as arquivo:
    ret = jsonpickle.encode(felix)
    arquivo.write(ret)

# Lendo o arquivo JSON/Pickle
with open("felix.json", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
    ret = jsonpickle.decode(conteudo)
    print(ret)
    print(ret.nome)
    print(ret.raca)
"""
