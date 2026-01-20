"""
Utilizando Lambdas

Conhecidas por Expressões Lambdas, ou simplesmente Lambdas, são funções
sem nome, ou seja, funções anônimas

# Função Python
def funcao(x):
    return 3 * x + 1

print(funcao(4))
print(funcao(7))

# Expressão Lambda
lambda x: 3 * x + 1

# E como utilizar a expressão lambda?
calc = lambda x: 3 * x + 1

print(calc(4))
print(calc(7))

# Podemos ter expressões lambdas com múltiplas entradas
nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
print(nome_completo('             Paula      ', 'Amancio     '))
print(nome_completo('John', '      Doe'))

# Em funções Python podemos ter nenhuma ou várias entradas. Em Lambdas também
amar = lambda: 'Como não amar Python?'
uma = lambda x: 3 * x + 1
duas = lambda x, y: (x + y) ** 0.5
tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)

# n = lambda x1, x1, ..., xn: <expressão>

print(amar())
print(uma(6))
print(duas(5, 7))
print(tres(3, 6, 9))

# OBS: Se passarmos mais argumentos do que parâmetros esperados teremos TypeError

# Outro exemplo
autores = [
    'Isaac Asimov',
    'Ray Bradbory',
    'Robert Heinlein',
    'Arthur C. Clarke',
    'Frank Herbert',
    'Orson Scott Card',
    'Douglas Adams',
    'H. G. Wells',
    'Leigh Brackett'
]

print(autores)
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print('\n=============\n')
print(autores)

# Função Quadrática
# f(x) = a * x ** 2 + b * x + c

# Definindo a função
def geradora_funcao_quadratica(a, b, c):
    '''
    Retorna a função f(x) = a * x ** 2 + b * x + c
    '''
    return lambda x: a * x ** 2 + b * x + c


teste = geradora_funcao_quadratica(2, 3, -5)
print(teste(0))
print(teste(1))
print(teste(2))
print(geradora_funcao_quadratica(3, 0, 1)(2))

# Também podemos usar lambdas dentro de uma estrutura de loop
lista_salarios = [1200, 950, 7000]

for salario in lista_salarios:
    resultado = lambda: salario * 2
    print(resultado())
"""

# ================

"""
Map

Com map, fazemos mapeamento de valores para função

import math


def area(raio):
    '''
    Calcula a área de um círculo com 'raio'

    Args:
        raio: float

    Returns:
        valor decimal da área do círculo com 'raio'
    '''
    return math.pi * (raio**2)


print(area(2))
print(area(5.3))

raios = [2, 5, 7.1, 0.3, 10, 44]

# Forma mais comum
areas = []
for raio in raios:
    areas.append(area(raio))

print(areas)

# Forma 2 - Map

# Map é uma função que recebe dois parâmetros: O primeiro a função, o segundo um iterável. Retorna um Map Object


areas = map(area, raios)
print(areas)
print(type(areas))
print(list(areas))

# Forma 3 - Map com Lambda
print(list(map(lambda r: math.pi * (r**2), raios)))

# OBS: Após utilizar a função map() depois da primeira utilização do resultado, ele zera

# Para fixar - Map

# Temos dados iteráveis:

# Dados: a1, a2, ..., an

# Temos uma função:

# Função: f(x)

# Utilizamos a função map(f, dados) onde map irá 'mapear' cada elementos dos dados e aplicar à função

# O Map Object: f(a1), f(a2), f(...), f(an)

# Mais um exemplo
cidades = [
    ("Berlim", 29),
    ("Cairo", 36),
    ("Buenos Aires", 19),
    ("Los Angeles", 26),
    ("Tokyo", 27),
    ("Nova Iorque", 28),
    ("Londres", 22),
]

print(cidades)

# f = 9 / 5 * c + 32

# Lambda

celsius_para_fahrenheit = lambda dado: (dado[0], (9/5) * dado[1] + 32)
print(list(map(celsius_para_fahrenheit, cidades)))
"""

# ================

"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleção

# Biblioteca para trabalhar com dados estatísticos
import statistics

# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)
print(f"Média: {media}")

# OBS: Assim como a função map(), a filter() recebe dois parâmetros, sendo
# uma função e um iterável

res = filter(lambda valor: valor > media, dados)
print(list(res))

# OBS: Assim como na função map(), após serem utilizados os dados de filter() eles são excluídos da memória

paises = [
    "",
    "Argentina",
    "",
    "Brasil",
    "Chile",
    "",
    "Colombia",
    "Equador",
    "",
    "",
    "Venezuela",
]
print(paises)

res = filter(lambda pais: len(pais) > 0, paises)
res = filter(None, paises)
print(list(res))

# A diferença entre map() e filter() é:
# map() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto mapeando a função para cada elemento do iterável
# filter() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto filtrando apenas os elementos de acordo com a função

# Exemplo mais complexo
usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": []},
]

# Filtrar os usuários que estão inativos no Twitter

# Forma 1
inativos = list(filter(lambda usuario: len(usuario["tweets"]) == 0, usuarios))
print(inativos)

# Forma 2
inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))
print(inativos)

# Combinar filter() e map()
nomes = ["Vanessa", "Ana", "Maria"]

# Devemos criar uma lista contendo 'Sua instrutora é' + nome, desde que cada nome tenha menos de 5 caracteres
lista = list(
    map(
        lambda nome: f"Sua instrutora é {nome}",
        filter(lambda nome: len(nome) < 5, nomes),
    )
)
print(lista)
"""
