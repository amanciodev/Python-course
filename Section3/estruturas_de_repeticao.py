"""
Loop for

Loop -> Estrutura de repetição
For -> Uma dessas estruturas

# OBS: Antes de começar essa aula, tente entender o máximo que conseguir da lógica e da syntax do código
# Não se preocupe em decorar tudo de primeiro, vamos nos aprofundar mais nas aulas seguintes e com a prática
# vamos aperfeiçoando nossos conhecimentos cada vez mais

# Syntax de um loop for em Python
# for item in iteravel:
    # Execução do bloco do loop

# Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

Exemplos de iteráveis:
- String
    nome = 'Paula Amancio'
- Lista
    lista = [1, 3, 5, 7, 9]
- Range
    numeros = range(1, 10)

nome = 'Paula Amancio'
lista = [1, 3, 5, 7, 7]
numeros = range(1, 10)

# Exemplo de for - 1 (Iterando sobre uma string)
for i in nome:
    print(i)

# Exemplo de for - 2 (Iterando sobre uma lista)
for numero in lista:
    print(numero)

# Exemplo de for - 3 (Iterando sobre um range)
for numero in range(2, 10):
    print(numero)

for numero in range(10, 0, -1):
    print(numero)

# E se eu quiser que a minha String apareça letra por letra uma do lado da outra ao invés de uma abaixo da outra?
nome = 'Paula Amancio'
for letra in nome:
    print(letra, end='')

# OBS: O parâmetro 'end' é um parâmetro da função print(), e não do loop. Não devemos cometer o erro de achar
# que só temos a função 'end' por estar dentro de um bloco do loop for. Podemos usar esse parâmetro a qualquer
# momento dentro do print

print('João', 'Amgarten', end='$')

'''
range(valor_inicial, valor_final, passo)
OBS: O valor final não é inclusivo
'''

# Podemos acessar os valores de uma string ou uma lista através do seu índice
nome = 'Paula Amancio'
for indice in range(len(nome)):
    print(nome[indice])

# Enumerate
nome = enumerate('João Amgarten')
# (0, 'J'), (1, 'o'), (2, 'ã'), (3, 'o') ...

for valor in nome:
    print(valor)

# Normalmente utilizamos o enumerate com duas variáveis dentro do loop
nome = enumerate('João Amgarten')
for indice, valor in nome:
    print(indice, valor)

# Também podemos fazer - (Mais comum utilizar enumerate dentro do próprio loop)
nome = 'João Amgarten'
for indice, valor in enumerate(nome):
    print(indice, valor)

# Quando nós não vamos utilizar uma variável, podemos "descartá-la" utilizando um underscore (_) como nome
nome = 'João Amgarten'
for _, valor in enumerate(nome):
    print(valor)

# Vamos combinar o nosso conhecimento de loops com o nosso conhecimento de inputs
quantidade = int(input('Quantas vezes esse loop deve rodar? '))
for n in range(1, quantidade+1):
    print(f'Imprimindo {n}')

# Agora, vamos combinar o nosso conhecimento de loops, com o nosso conhecimento de inputs e o nosso conhecimento
# de operações matemáticas

quantidade = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0

for n in range(1, quantidade+1):
    numero = int(input(f'Informe o {n}º de {quantidade} valores: '))
    soma = soma + numero

print(f'A soma é: {soma}')

# Também podemos usar emojis no nosso código
# Tabela de Emojis Unicode: https://unicode.org/emoji/charts/full-emoji-list.html#1f603

# Unicode original: U+1F603
# Unicode Python: U0001F603  # Apenas substituímos o sinal de + por três zeros (000) e adicionamos uma barra invertida no início

emoji = '\U0001F603'
for num in range(1, 11):
    print(f'{emoji * num}')
"""

# =======================

"""
Loop While

# Syntax de um loop while em Python
# while expressao_booleana:
    # Execução do bloco do while

O bloco do while será repetido enquanto a expressão booleana for verdadeira
Expressão booleana é toda expressão onde o resultado é verdadeiro ou falso

# Exemplo 1
number = 1
while number <= 10:
    print(number)
    number += 1

# OBS: Em um loop while, é importante que cuidemos do critério de parada para não causar um loop infinito

# Exemplo 2
answer = ''
while answer != 'yes':
    answer = input('Do you want to stop the program? (yes/no): ')
"""

# =======================

"""
Saindo de loops com break

Utilizamos o break para sair de loops de maneira projetada

# Exemplo 1
for number in range(1, 11):
    if number == 6:
        break
    else:
        print(number)

# Exemplo 2
while True:
    user_input = input('Insert "quit" to quit: ')
    if user_input == 'quit':
        break
"""
