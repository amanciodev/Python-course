"""
Definindo Funções
    - Funções são pequenas partes de código que realizam tarefas específicas;
    - Pode ou não receber entradas de dados e retornar uma saída de dados;
    - Muito uteis para executar procedimentos similares por repetidas vezes;

# OBS: Se você escrever uma função que realiza várias tarefas dentro dela;
# é bom fazer uma verificação para que a função seja simplificada.
# Já utilizamos várias funções desde que inicamos este curso:
    - print()
    - len()
    - max()
    - min()
    - count()
    - e muitas outras;

# Exemplo de utilização de funções:
cores = ['verde', 'amarelo', 'azul', 'branco']

# Utilizando a função integrada (Built-in) do Python print()
print(cores)
curso = 'Curso Python'
print(curso)
cores.append('roxo')
print(cores)

curso.append('Mais dados...') # AttributeError
print(curso)
cores.clear()
print(cores)

# DRY - Don't Repeat Yourself - Não repita você mesmo / Não repita o seu código
# Mas então, como definir funções?

Em Python, a forma geral de definir uma função é:
def nome_da_funcao (parametros_de_entrada):
    bloco_da_funcao

Onde:
    - nome_da_funcao -> SEMPRE, com letras minúsculas, e se for nome composto, separado por underline (Snake Case);
    - parametros_de_entada -> Opcionais, onde tendo mais de um, cada um separado por vírgula, podendo ser opcionais ou não;
    - bloco_da_funcao -> Também chamado de corpo da função ou implementação, é onde o processamento da função acontece.
    - Neste bloco, pode ter ou não retorno da função.

OBS: Veja que para definir uma função, utilizamos a palavra reservada 'def' informando ao Python que
estamos definindo uma função. Também abrimos o bloco de código com o já conhecido dois pontos que é
utilizado em Python para definir blocos.

# Definindo a primeira função
def diz_o1():
    print('oi!')

OBS:
1 - Veja que, dentro das nossas funções podemos utilizar outras funções;
2 - Veja que nossa função só executa 1 tarefa, ou seja, a única coisa que ela faz é dizer oi;
3 - Veja que esta função não recebe nenhum parâmetro de entrada;
4 - Veja que esta função não retorna nada;

# Utilizando funções
# Chamada de execução
diz_oi()

# ATENÇÃO: Nunca esqueça de utilizar os parênteses ao executar uma função.
# Exemplo:
# Errado!
diz_oi

# Certo
diz_oi()

# Exemplo 2
def cantar_parabens():
    print('Parabéns pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print('Viva o aniversariante!')

#for n in range(5):
# cantar_parabens()
# Em Python, podemos inclusive criar variáveis do tipo de uma função e executar esta função através da variável
canta = cantar_parabens
canta()
"""

# ========================

"""
Funções com retorno

numeros = [1, 2, 3]
ret_pop = numeros.pop()
print(f'Retorno de pop: {ret_pop}')

ret_pr = print(numeros)
print(f'Retorno de print: {ret_pr}')

# Exemplo de uma função
def quadrado_de_7():
    print(7 ** 2)

ret = quadrado_de_7()
print(ret)

# OBS: Em Python, quando uma função não retorna nenhum valor, o retorno é None

# OBS: Funções Python que retornam valores, devem retornar estes valores com a
# palavra reservada 'return'

# OBS: Não precisamos necessariamente criar uma variável para receber o retorno
# de uma função. Podemos passar a execução da função para outras funções

# Vamos refatorar a função anterior para que ela retorne o valor
def quadrado_de_7():
    return 7 ** 2

# Criamos uma variável para receber o retorno da função
ret = quadrado_de_7()
print(f'Retorno: {ret}')
print(f'Retorno: {quadrado_de_7()}')

# Refatorando a primeira função
def diz_oi():
    return 'Oi!'

alguem = "Paula!"
print(diz_oi())
print(alguem)

# OBS: Sobre a palavra reservada 'return':
#   1. Ela finaliza a função, ou seja, ela sai da execução da função
#   2. Podemos ter, em uma função, diferentes returns
#   3. Podemos, em uma função, retornar qualquer tipo de dado e até mesmo múltiplos valores

# Exemplo 1 - Ela finaliza a função, ou seja, ela sai da execução da função
def diz_oi():
    print('Estou sendo executado antes do retorno...')
    return 'Oi!'
    print('Estou sendo executado após o retorno...')

print(diz_oi())

# Exemplo 2 - Podemos ter, em uma função, diferentes returns
def nova_funcao():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'

print(nova_funcao())

# Exemplo 3 - Podemos, em uma função, retornar qualquer tipo de dado e até mesmo múltiplos valores
def outra_funcao():
    return 2, 3, 4, 5

num1, num2, num3, num4 = outra_funcao()
print(num1, num2, num3, num4)

print(outra_funcao())
print(type(outra_funcao))

# Vamos criar uma função para jogar a moeda
from random import random

def joga_moeda():
    # Gera um valor pseudo-randômico entre 0 e 1
    valor = random()
    if valor > 0.5:
        return f'Cara'
    return f'Coroa'

for i in range(5):
    print(joga_moeda())

# Más práticas comuns na utilização do retorno, considerado codificação desnecessária
def eh_impar():
    numero = 6
    if numero % 2 != 0:
        return True
    return False

print(eh_impar())

def conta_ate_10():
    contagem = 1
    while contagem <= 10:
        print(contagem, end=' ')
        contagem += 1

conta_ate_10()
"""

# ========================

"""
Funções com parâmetros (de entrada)

- Funções que recebem dados para serem processados dentro da mesma

Se nós pensarmos em um programa qualquer, geralmente temos:

entrada -> processamento -> saída

Se nós pensarmos em função, já sabemos que temos funções que:
    - Não possuem entrada
    - Não possuem saída
    - Possuem entrada, mas não possuem saída
    - Não possuem entrada, mas possuem saída
    - Possuem entrada e saída

# Refatorando uma função
def quadrado(numero):
    return numero * numero

print(quadrado(7))
print(quadrado(2))
print(quadrado(5))

retorno = quadrado(6)
print(retorno)

# Refatorando uma função
def soma_numero(numero):
    return numero + 2

print(soma_numero(7))
print(soma_numero(2))
print(soma_numero(5))

retorno = soma_numero(6)
print(retorno)
print(soma_numero())  # TypeError

# Refatorar a função cantar_parabens
def cantar_parabens(aniversariante):
    print('Parabéns pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva a/o {aniversariante}! 🥳🥳')

cantar_parabens('Paula')

# Funções podem ter n parâmetros de entrada. Ou seja, podemos receber como entrada
# em uma função quantos parâmetros forem necessários. Eles são separados por vírgulas

# Exemplos
def soma(a, b):
    return a + b

def multiplica(num1, num2):
    return num1 * num2

def mostra_mensagem(num1, b, msg):
    return (num1 + b) * msg

print(soma(2, 5))
print(soma(10, 20))

print("=========")

print(multiplica(4, 5))
print(multiplica(2, 8))

print("=========")

print(mostra_mensagem(3, 2, 'Python '))
print(mostra_mensagem(0, 2, 'Python '))

# OBS: Se nós informarmos um número errado de parâmetros ou argumentos, teremos TypeError

# print(soma(2, 3, 4))  # TypeError - Passando argumentos a mais
# print(soma(4))  # TypeError - Passando argumentos a menos

# Nomeando parâmetros
def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'

print(nome_completo('Patricia', 'Amaral'))

# A diferença entre parâmetros e argumentos:
# - Parâmetros são variáveis declaradas na definição de uma função
# - Argumentos são dados passados durante a execução de uma função

# A ordem dos parâmetros importa!
nome = 'Luíza'
sobrenome = 'Cavalcante'
print(nome_completo(nome, sobrenome))
print(nome_completo(sobrenome, nome))

# Argumentos nomeados (Keyword Arguments)
# Caso utilizemos nomes dos parâmetros nos argumentos para informá-los, podemos
# utilizar qualquer ordem

print(nome_completo(nome=nome, sobrenome=sobrenome))
print(nome_completo(nome='Corey', sobrenome='Taylor'))
print(nome_completo(sobrenome='Root', nome='Jim'))

# Erro comum na utilização do return
def soma_impares(numeros):
    total = 0
    for numero in numeros:
        if numero % 2 != 0:
            total += numero
        return total  # Esse return não deveria estar aqui

lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))
"""

# ========================

"""
Documentando funções com Docstrings

OBS: Podemos ter acesso à documentação de uma função em Python utilizando a propriedade especial __doc__

Podemos ainda fazer acesso à documentação com a função help()

# Exemplos
def diz_oi():
    '''
    Uma função simples que retorna uma string 'Oi!'
    '''
    return 'Oi!'

print(diz_oi())

def exponencial(numero, potencia=2):
    '''
    Função que retorna por padrão o quadrado de 'número' ou 'número' à 'potência' informada.
    :param numero: Número que desejamos gerar o exponencial
    :param potencia: Potência que queremos gerar o exponencial. Por padrão é 2.
    :return: Retorna o exponencial de 'numero' por 'potencia'
    '''
    return numero ** potencia

# Exemplo Docstring da Google
def exponencial(numero, potencia=2):
    '''
    Função que retorna por padrão o quadrado de 'número' ou 'número' à 'potência' informada.

    Args:
        numero: Número que desejamos gerar o exponencial
        potencia: Potência que queremos gerar o exponencial. Por padrão é 2.

    Returns:
        Retorna o exponencial de 'numero' por 'potencia'
    '''
    return numero ** potencia

print(exponencial(5, 3))
"""

# ========================

"""
Entendendo o *args

- O *args é um parâmetro como outro qualquer. Isso significa que você poderá
chamar de qualquer coisa, desde que comece com asterisco.

Exemplo:
*xis

Mas, por convenção, utilizemos *args oara definí-lo

Mas o que é o *args?

O parâmetro *args utilizado em uma função, coloca valores extras informados como
entrada em uma tupla. Então desde já lembre-se que tuplas são imutáveis

# Exemplos
# O que já conhecemos
def soma_todos_numeros(num1=1, num2=2, num3=3):
    return num1 + num2 + num3


print(soma_todos_numeros())
print(soma_todos_numeros(4, 6, 9))
print(soma_todos_numeros(4, 6))
# print(soma_todos_numeros(4, 6, 9, 5))  # TypeError

# *Args
def soma_todos_numeros(*args):
    # print(args)
    # return sum(args)
    total = 0
    contagem = 0
    while contagem < len(args):
        total += args[contagem]
        contagem += 1
    return total


print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(2, 3))
print(soma_todos_numeros(2, 3, 4))
print(soma_todos_numeros(2, 3, 4, 5))
print(soma_todos_numeros(23.4, 12.5))

# Refatorando a função soma_todos_numeros()
def soma_todos_numeros(nome, email, *args):
    return len(args)


print(soma_todos_numeros("John", "john@gmail.com", 1))
print(soma_todos_numeros("John", "john@gmail.com", 2, 3))
print(soma_todos_numeros("John", "john@gmail.com", 2, 3, 4))
print(soma_todos_numeros("John", "john@gmail.com", 2, 3, 4, 5))

# Outro exemplo de utilização do *args
def verifica_info(*args):
    if 'Python' in args and 'Programming' in args:
        return 'Você está aprendendo programação em Python!'
    return 'Não era suposto você estar aqui...'


print(verifica_info())
print(verifica_info(1, True, 'Python', 'Programming'))
print(verifica_info(1, 'C++', 'Programming', 3.1415))

# E se tentarmos passar uma lista de inteiros para o args?
def soma_todos_numeros(*args):
    print(args)
    return sum(args)


numeros = [1, 2, 3, 4, 5, 6, 7]
# print(soma_todos_numeros(numeros))  # TypeError

# OBS: Devemos nos lembrar que o args transforma nosso argumento em uma tupla,
# logo, esse exemplo da lista retornará um TypeError, pois não é possível
# somar um objeto com uma lista

# Para isso, precisamos desempacotar os valores da nossa lista e passar cada
# um deles para o nosso args

# Desempacotamento - Forma MENOS Comum
num1, num2, num3, num4, num5, num6, num7 = numeros
print(soma_todos_numeros(num1, num2, num3, num4, num5, num6, num7))

# Desempacotamento - Forma MAIS Comum (usando *)
print(soma_todos_numeros(*numeros))

# OBS: O asterisco serve para que informemos ao Python que estamos
# passando como argumento uma coleção de dados. Desta forma, ele saberá
# que precisará antes desempacotar esses dados
"""

# ========================

"""
**kwargs

Poderíamos chamar este parâmetro de **xis, mas por convenção chamamos de **kwargs

Este é só mais um parâmetro, mas diferente do *args que coloca os valores extras em uma tupla, o **kwargs
exige que utilizemos parâmetros nomeados, e transforma esses parâmetros extras em um dicionário

# Exemplo
def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f"A cor favorita de {pessoa} é {cor}")


cores_favoritas(marcos="verde", julia="amarelo", fernanda="azul", vanessa="branco")

# OBS: Os parâmetros *args e **kwargs NÃO são obrigatórios
cores_favoritas()
cores_favoritas(joao='marrom')

# Exemplo mais complexo
def cumprimento_especial(**kwargs):
    print("====", kwargs)
    if "user" in kwargs and kwargs["user"] == "Paula":
        return "Você recebeu um cumprimento Pythônico, Paula!"
    elif "user" in kwargs:
        return f"{kwargs['user']} é um Geek!"
    return "Não tenho certeza do que fazer com você..."


print(cumprimento_especial())
print(cumprimento_especial(user='Paula'))
print(cumprimento_especial(user='João'))
print(cumprimento_especial(user='Oi'))
print(cumprimento_especial(aleatorio='Oi'))

# Nas nossas funções, podemos ter (NESTA ORDEM)
# - Parâmetros obrigatórios
# - *args
# - Parâmetros defaults (parâmetros não obrigatórios)
# - **kwargs


def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f"{nome} tem {idade} anos")
    print(args)
    if solteiro:
        print("Solteiro")
    else:
        print("Casada")
    print(kwargs)


minha_funcao(18, "Julia")
print("==========")
minha_funcao(18, "Jones", 4, 5, 3, solteiro=True)
print("==========")
minha_funcao(34, "Felipe", eu="Não", voce="Vai")
print("==========")
minha_funcao(19, "Carla", 9, 4, 3, java=False, python=True)

# Entenda o porquê é importante manter a ordem dos parâmetros na declaração

# Função com a ordem correta de parâmetros
def mostra_info(a, b, *args, instrutor='Geek', **kwargs):
    return [a, b, args, instrutor, kwargs]

a = 1
b = 2
args = (3,)
print(mostra_info(a, b, args, sobrenome="Doe", cargo="Instrutor"))
# A=1, B=2, Args=(3, ), Instrutor='Geek', kwargs={'sobrenome': 'Doe', 'cargo': 'Instrutor'}
print(mostra_info(a, b, 3, sobrenome="Doe", cargo="Instrutor"))

# Desempacotar com **kwargs
def mostra_nomes(**kwargs):
    return f'{kwargs['nome']} {kwargs['sobrenome']}'

nomes = {'nome': 'Corey', 'sobrenome': 'Taylor'}
print(mostra_nomes(**nomes))

def soma_multiplos_numeros(a, b, c, **kwargs):
    print(a + b + c)

lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}
dicionario = dict(a=1, b=2, c=3)

soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)
soma_multiplos_numeros(**dicionario)

# OBS: Os nomes da chaves em um dicionário devem ser os mesmos dos parâmetros da função
# dicionario = dict(d=1, e=2, f=3)  # TypeError
# soma_multiplos_numeros(**dicionario)
soma_multiplos_numeros(**dicionario, lang='Python')
"""
