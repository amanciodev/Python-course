"""
Listas

Listas em Python funciona como vetores/matrizes (arrays) em outras linguagens também, com a diferença
de serem DINÂMICOS e também de podermos colocar QUALQUER tipo de dado.

Listas em Python:
- Dinâmico: Não possuem tamanho fixo; Ou seja, podemos criar a lista e simplesmente ir adicionando elementos;
- Qualquer tipo de dado: Não possuem tipo de dado fixo; Ou seja, podemos colocar qualquer tipo de dado;

As listas em Python são representadas por colchetes: []

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['C', 'u', 'r', 's', 'o', ' ', 'P', 'y', 't', 'h', 'o', 'n']
lista3 = []
lista4 = list(range(11))
lista5 = list('Curso Python')

# Podemos facilmente checar se determinado valor está contido na lista
num = 7
if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')

# Podemos facilmente ordenar uma lista
print(lista1)
lista1.sort()
print(lista1)

# Podemos facilmente contar o número de ocorrências de um valor em uma lista
print(lista1.count(1))
print(lista1.count('o'))

# Adicionar elementos em listas
# Para adicionar elementos em listas, utilizamos a função .append()
# OBS: A função .append() ela adiciona elementos no final da nossa lista
print(lista1)
lista1.append(42)
print(lista1)

# OBS: Com append, nós só conseguimos adicionar 1 elemento por vez
# lista1.append(12, 34, 56)  # Erro

# Também conseguimos adicionar uma lista dentro de outra lista
lista1.append([8, 3, 1])
print(lista1)

if [8, 3, 1] in lista1:
    print('Encontrei a lista [8, 3, 1]')
else:
    print('Não consegui encontrar a lista')

# Também podemos adicionar vários valores na nossa lista com .extend()
# O método extend só funciona com iteráveis, não conseguimos colocar valores únicos nele
print(lista1)
lista1.extend([123, 44, 67])  # Coloca cada elemento da lista como valor adicional à nossa lista1
lista1.extend('Paula')  # Também conseguimos inserir uma string
print(lista1)

# Podemos inserir um novo elemento na lista informando a posição do índice
# OBS: Isso não substitui o valor inicial. O mesmo será deslocado para a direita da lista
print(lista1)
lista1.insert(2, True)
print(lista1)

# Podemos facilmente juntar duas listas
lista6 = lista1 + lista2
print(lista6)

# O resultado de somar duas listas é o mesmo se fizermos .extend()
lista1.extend(lista2)
print(lista1)

# Podemos facilmente inverter uma lista
print(lista1)
print(lista2)

lista1.reverse()
lista2.reverse()

print('======= DEPOIS DE INVERTER =======')

print(lista1)
print(lista2)

# Também podemos inverter uma lista da mesma maneira que invertemos uma string
print(lista1[::-1])
print(lista2[::-1])

# Copiar uma lista
lista6 = lista2.copy()
print(lista6)

# Se quisermos saber o tamanho de uma lista (quantos elementos temos nela) usamos len() => len significa length em inglês
# OBS: O len() começa a contar a partir do 1, e não do 0
print(len(lista1))

# Podemos remover facilmente o último elemento de uma lista
print(lista5)
lista5.pop()
print(lista5)

# O pop não somente remove o último elemento, mas também o retorna
print(lista5.pop())

# Podemos remover um elemento pelo índice
# OBS: Os elementos à direita desse índice serão deslocados para a esquerda
# OBS: Se não houver elemento no índice informado, teremos o erro IndexError
print(lista5)
lista5.pop(2)
print(lista5)

# Podemos remover todos os elementos da nossa lista (zerar a lista)
print(lista5)
lista5.clear()
print(lista5)

# Podemos repetir elementos em uma lista utilizando o sinal *
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

# Podemos converter uma string para uma lista
# Exemplo 1
curso = "Curso de Python com João Amgarten"
print(curso)
curso = curso.split()
print(curso)

# Por padrão, o .split() separa os elementos da lista pelo espaço entre elas

# Exemplo 2
curso = "Curso,de,Python,com,João,Amgarten"
print(curso)
curso = curso.split(',')
print(curso)

# Podemos fazer ao contrário e converter uma lista em uma string
lista6 = ['Curso', 'de', 'Python', 'com', 'o', 'João', 'Amgarten']
print(lista6)
print(type(lista6))

curso = ' '.join(lista6)
print(curso)
print(type(curso))

# Também podemos colocar outros caracteres ao invés do espaço como separadores na hora de converter uma lista pra uma string
lista6 = ['Curso', 'de', 'Python', 'com', 'o', 'João', 'Amgarten']

curso = '$'.join(lista6)
print(curso)

# Podemos realmente colocar qualquer tipo de dado em uma lista, inclusive misturando esses dados
lista6 = [1, 2.34, True, 'Python', 'd', [1, 2, 3], 47383902145]
print(lista6)
print(type(lista6))

# Iterando sobre listas
# Exemplo 1 - Utilizando For
soma = 0
for elemento in lista4:
    print(elemento)
    soma = soma + elemento
print(soma)

# OBS: Nós só conseguimos usar + com números e números, ou strings e strings, nunca tentando somar uma string com um número

# Exemplo 2 - Utilizando While
lista_de_utilizadores = []

while True:
    nome_utilizador = input('Digite o nome do utilizador ("sair" para sair): ')
    if nome_utilizador == 'sair':
        break
    lista_de_utilizadores.append(nome_utilizador)

print(lista_de_utilizadores)

# Utilizando variáveis em listas
numeros = [1, 2, 3, 4, 5]
print(numeros)

num1, num2, num3, num4, num5 = 1, 2, 3, 4, 5

numeros = [num1, num2, num3, num4]
print(numeros)

# Fazemos acesso aos elementos de forma indexada
#           0         1         2        3
cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[0])  # verde
print(cores[1])  # amarelo
print(cores[2])  # azul
print(cores[3])  # branco

# Podemos também fazer acesso aos elementos de forma indexada reversa
# Para entender melhor o índice negativo, pense na lista como uma
# contagem humana, onde começamos a contar a partir do 1, ao invés
# do 0

print(cores[-1])  # branco
print(cores[-2])  # azul
print(cores[-3])  # amarelo
print(cores[-4])  # verde

cores = ['verde', 'amarelo', 'azul', 'branco']

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice += 1

# Mostrar o índice e o valor em um loop for
for indice, cor in enumerate(cores):
    print(indice, cor)

# Listas aceitam valores repetidos
lista = []
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
lista.append(42)

print(lista)

# Outros métodos não tão importantes, mas também úteis

# Encontrar o índice de um elemento na lista
numeros = [5, 6, 7, 8, 9, 10]
print(numeros.index(6))
print(numeros.index(9))

# OBS: Caso não tenha este elemento na lista, será apresentado ValueError
print(numeros.index(19))

# Podemos fazer uma busca dentro de um range, ou seja, qual índice começar a procurar
numeros = [5, 6, 7, 5, 8, 9, 10]
print(numeros.index(5, 1))  # Buscando a partir do índice 1, ignorando a busca do primeiro elemento da lista
print(numeros.index(5, 2))  # Buscando a partir do índice 2, ignorando a busca do primeiro elemento da lista
# OBS: Caso não tenha este elemento na lista, será apresentado ValueError


# Podemos fazer busca dentro de um range com início/fim
print(numeros.index(8, 3, 6))  # Buscar o índice do valor 8, entre os índices 3 a 6

# Revisão de slicing
# lista[inicio:fim:passo]
# range(inicio:fim:passo)

# Trabalhando com slice de lista com o parâmetro 'início'
lista = [1, 2, 3, 4]
print(lista[1:])  # Iniciando no índice 1 e pegando todos os elementos restantes
print(lista[::])  # Pegando tudo da lista

# Trabalhando com slice de lista com o parâmetro 'fim'
print(lista[:2])  # Começando em 0, pega até o índice 2 - 1 (Lembre-se, o fim não é inclusivo)
print(lista[:4])  # Começando em 0, pega até o índice 4 - 1 (Lembre-se, o fim não é inclusivo)
print(lista[1:3])  # Começando em 1, pega até o índice 3 - 1 (Lembre-se, o fim não é inclusivo)

# Trabalhando com slice de lista com o parâmetro 'passo'
print(lista[1::2])  # Começa em 1, vai até o final, de 2 em 2
print(lista[::2])  # Começa em 0, vai até o final, de 2 em 2

# Invertendo valores em uma lista usando variáveis - Exemplo 1
direcoes = ['Esquerda', 'Direita']
print(direcoes)

direcoes[0], direcoes[1] = direcoes[1], direcoes[0]

print(direcoes)

# Invertendo valores em uma lista usando variáveis - Exemplo 2
direcoes = ['Esquerda', 'Direita']
print(direcoes)
direcoes.reverse()
print(direcoes)

# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho
# * Se os valores forem todos inteiros ou reais
lista = [1, 2, 3, 4, 5, 6]

print(sum(lista))  # Soma
print(max(lista))  # Valor Máximo
print(min(lista))  # Valor Mínimo
print(len(lista))  # Tamanho

# Desempacotamento de listas
lista = [1, 2, 3]

num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)

# OBS: Se tivermos um número diferente de elementos na lista ou variáveis para receber os dados, teremos ValueError
lista = [1, 2, 3, 4]

num1, num2, num3 = lista  # Erro

print(num1)
print(num2)
print(num3)

# Copiando uma lista para outra (Shallow Copy e Deep Copy)
# Forma 1 - Deep Copy
lista = [1, 2, 3]
print('Original:', lista)

nova = lista.copy()
print('Cópia:', nova)

nova.append(4)

print("=============")

print('Original:', lista)
print('Cópia:', nova)

# Veja que ao utilizarmos lista.copy(), copiamos os dados da lista para uma nova lista, mas elas
# ficaram totalmente independentes, ou seja, modificando uma lista, não afeta a outra. Isso em Python
# é chamado de Deep Copy (Cópia Profunda)

# Forma 2 - Shallow Copy
lista = [1, 2, 3]
print('Original:', lista)

nova = lista
print('Cópia:', nova)

nova.append(4)

print("=============")

print('Original:', lista)
print('Cópia:', nova)

# Veja que utilizamos a cópia via atribuição e copiamos os dados da lista para a nova lista, mas
# após realizar modificação em uma das listas, essa modificação se refletiu em ambas as listas.
# Isso em Python é chamado de Shallow Copy (Cópia Rasa)
"""
