"""
Print -> Mostra na tela o que estiver dentro dos (). Chamado também de output

print("Hello, World!")
"""

# =====================================

"""
Variáveis: Um valor armazenado em um endereço de memória do seu computador
Imagine como se fossem gavetas com etiquetas
meu_nome = "João"
minha_idade = "21"

# Vamos combinar o print com as nossas variáveis:
print(meu_nome)
print(minha_idade)
"""

# =====================================

"""
Recebendo um input (entrada de dados) do usuário

nome = input()
print(nome)

# Podemos também deixar uma mensagem no terminal
nome = input('Digite o seu nome: ')
print(nome)
"""

# =====================================

"""
TIPOS PRIMITIVOS

# Tipo Int
print(10)
print(10 + 1)
print(10 - 1)
print(10 * 2)
print(10 / 2)

x = 10
x = x + 1
x += 1

x = x - 1
x -= 1

# Números grandes se usam underscore
print(10_000_000)
print(type(10))
"""

# =====================================

"""
Tipo Float

Tipo real, decimal

Casas decimais

OBS: O separador de casas decimais na programação é o ponto, não a vírgula

# Errado
peso = 70,00
print(peso)

# Certo
peso = 25.50
print(peso)
print(type(peso))

# Podemos usar todas as operações matemáticas que aprendemos com o int
print(10.25)
print(10.25 + 1.30)
print(10.10 - 1.50)
print(10.20 * 2.50)
print(10.10 / 2.30)

peso = 10.0
peso = peso + 1
print(peso)

# Podemos converter um float para um int (casting)
numero = 10.0
print(type(numero))
resultado = int(numero)
print(type(resultado))

# Também podemos fazer tudo em um único linha
print(type(int(10.2)))

# OBS: Ao converter valores floats para inteiros, nós perdemos precisão
novo_numero = 15.77
print(int(novo_numero))

# Pode parecer bobo, mas vamos olhar na prática
salario1 = 2.56
salario2 = 3.67
total1 = salario1 + salario2
print(total1)

total2 = int(salario1) + int(salario2)
print(total2)

# Também podemos converter de inteiro para float
meu_inteiro = 20
print(float(meu_inteiro))
"""

# =====================================

"""
Tipo Booleano

Álgebra booleana, criada por George Boole

2 constantes, Verdadeiro ou Falso

True -> Verdadeiro
False -> Falso

OBS: Em Python, sempre com a inicial maiúscula

Errado:
true, false

Certo:
True, False

ativo = False
print(ativo)
print(type(ativo))

# Operações Básicas

# Negação (not)
# Fazendo a negação, se o valor booleano for verdadeiro, o resultado será falso, se for falso
# o resultado será verdadeiro. Ou seja, sempre ao contrário
print(False)
print(not False)
print(True)
print(not True)

# Ou (or)
# É uma operação binária, ou seja, depende de dois valores. Ou um ou outro deve ser verdadeiro.
# True or True -> True
# True or False -> True
# False or True -> True
# False or False -> False

ativo = True
logado = False

print(ativo or logado)

# E (and)
# Também é uma operação binária, ou seja, depende de dois valores. Ambos os valores devem ser verdadeiros
# True and True -> True
# True and False -> False
# False and True -> False
# False and False -> False

# Operadores relacionais
# > Maior
# < Menor
# == Igual a
# >= Maior ou igual a
# <= Menor ou igual a
# != Diferente de

print(5 > 6)  # False
print(5 < 6)  # True
print(5 == 6)  # False
print(5 >= 6)  # False
print(5 <= 6)  # True
print(5 != 6)  # True
"""

# =====================================

"""
Tipo String

Em Python, um dado é considerado um tipo string sempre que:

- Estiver entre aspas simples -> 'uma string', '234', 'a', 'True', '42.3'
- Estiver entre aspas duplas -> "uma string", "234", "a", "True", "42.3"
- Estiver entre aspas simples triplas -> '''uma string''', '''234''', '''a''', '''42.3'''
"""
# - Estiver entre aspas duplas triplas -> """uma string""", """234""", """a""", """42.3"""
"""
  0    1    2    3    4    5    6    7    8    9   10   11
['C', 'u', 'r', 's', 'o', ' ', 'P', 'y', 't', 'h', 'o', 'n']


curso = "Curso Python"
nome = "Paula"

# Acessando os valores de uma string a partir do seu índice (index)
print(curso[9])

# Slicing de Strings
print(curso[0:5])  # Inicio : Final + 1
print(nome[0:20])

# Inverter uma string
print(nome[::-1])  # Comece do primeiro, vá até o último elemento, e inverta

# Split
nome = "Paula Aboutamancio"
splitted = nome.split()

# Replace
print(nome.replace('o', 'e'))
print(type('Paula'))
"""
