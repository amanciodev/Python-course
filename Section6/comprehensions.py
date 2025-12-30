# Usamos parênteses ()
#   - Para criar tuplas (não é obrigatório)
#   - Para chamada de funções
#   - Exemplos:
#       - print()
#       - sorted()
#       - max()
#       - min()
#       - len()

# Usamos colchetes []
#   - Para criar listas
#   - Para indexações
#   - Para slicing

# Usamos chaves {}
#   - Para criar dicionários
#   - Para criar conjuntos

"""
List Comprehension

- Utilizando List Comprehension nós podemos gerar novas listas com dados processaods a partir de outro iterável

# Sintaxe da List Comprehension
[dado for dado in iteravel]

# Exemplos
numeros = [1, 2, 3, 4, 5]
resultado = [numero * 10 for numero in numeros]
print(resultado)

Para entender melhor o que está acontecendo devemos dividir a expressão em duas partes:
    - A primeira parte: for numero in numeros
    - A segunda parte: numero * 10

numeros = [1, 2, 3, 4, 5]

res = [numero / 2 for numero in numeros]
print(res)

numeros = [1, 2, 3, 4, 5]

def funcao(valor):
    return valor * valor

res = [funcao(numero) for numero in numeros]
print(res)

# List Comprehension vs Loops

# Loops
numeros = [1, 2, 3, 4, 5]
numeros_dobrados = []

for numero in numeros:
    numero_dobrado = numero * 2
    numeros_dobrados.append(numero_dobrado)

print(numeros_dobrados)

# List Comprehension
print([numero * 2 for numero in numeros])
print([numero * 2 for numero in [1, 2, 3, 4, 5]])

# Outros exemplos:

# 1.
nome_curso = 'Curso Python'
print([letra.upper() for letra in nome_curso])

# 2.
amigos = ['maria', 'júlia', 'pedro', 'guilherme', 'vanessa']
print([amigo.title() for amigo in amigos])

# 3.
print([numero * 3 for numero in range(1, 10)])

# 4.
print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

# Nós também podemos adicionar estruturas condicionais lógicas às nossas List Comprehensions

# Exemplos

# 1.
numeros = [1, 2, 3, 4, 5, 6]

pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

print(pares)
print(impares)

# Refatoração
# Qualquer número par módulo de 2 é 0, e 0 em Python é False. Not False = True
pares = [numero for numero in numeros if not numero % 2]

# Qualquer número impar módulo de 2 é 1, e 1 em Python é True
impares = [numero for numero in numeros if numero % 2]

print(pares)
print(impares)

# 2.
res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)
"""

# ================

"""
Listas aninhadas (Nested Lists)

- Algumas linguagens de programação (C / Java) possuem uma estrutura de dados chamadas de arrays:
    - Unidimensionais (Arrays / Vetores)
    - Multidimensionais (Matrizes)

Em Python nós temos as listas:
numeros = [1, 'b', 3.234, True, 5]

# Exemplos
#                                                    L C
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matriz 3x3
print(listas)
print(type(listas))

# Como fazemos para acessar os dados?
print(listas[0][1])  # 2
print(listas[2][1])  # 8

# Iterando com loops em uma lista aninhada
for lista in listas:
    for num in lista:
        print(num)

# List Comprehension
[[print(valor) for valor in lista] for lista in listas]

# Outros exemplos

# Gerando um tabuleiro/matriz 3x3
tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

# Gerando valores iniciais
print([['*' for numero in range(1, 4)] for linha in range(1, 4)])

# Gerando jogadas para o jogo da velha
velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)
"""

# ================

"""
Set Comprehension

lista = [1, 2, 3, 4, 5]
conjunto = {1, 2, 3, 4, 5}

# Exemplos
numeros = {x ** 2 for x in range(10)}
print(numeros)

# Outro exemplo
numeros = {num for num in range(1, 6)}
print(numeros)
print(type(numeros))

# DESAFIO! Faça uma alteração na estrutura abaixo para gerar números pulando de 2 em 2
print({numero for numero in range(0, 21, 2)})

# Para finalizar
letras = sorted({letra for letra in 'Curso Python'})
print(letras)
"""

# ================

"""
Dictionary Comprehension

Pense no seguinte:

Se quisermos criar uma lista fazemos:
lista = [1, 2, 3, 4]

Se quisermos criar uma tupla:
tupla = (1, 2, 3, 4)

Se quisermos criar um set (conjunto):
conjunto = {1, 2, 3, 4}

Se quisermos criar um dicionário:
dicionario = {'1': 'a', '2': 'b', '3': 'c', '4': 'd'}

# Sintaxe
{chave: valor for valor in iteravel}

# Exemplos

# 1. Usando dicionários
numeros = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
quadrados = {chave: valor ** 2 for chave, valor in numeros.items()}
print(numeros.items())
print(quadrados)

# 2. Usando listas
numeros = [1, 2, 3, 4, 5]
quadrados = {valor: valor ** 2 for valor in numeros}
print(quadrados)

# OBS: Vale a pena lembrar que dicionários não repetem chaves
numeros = [1, 2, 3, 4, 5, 1, 2, 3]
quadrados = {valor: valor ** 2 for valor in numeros}
print(quadrados)

# 3. Usando strings
chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)

# Exemplos com lógica condicional
numeros = [1, 2, 3, 4, 5]
res = {num:('par' if num % 2 == 0 else 'impar') for num in numeros}
print(res)
"""
