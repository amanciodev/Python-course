"""
Erros mais comuns em Python

ATENÇÃO! É importante prestar atenção e aprender a ler as saídas de erros geradas
pela execução do nosso código.

Os erros mais comuns:

1. SyntaxError -> Ocorre quando o Python encontra um erro de síntaxe. Ou seja, você
escreveu algo que o Python não reconhece como parte da linguagem

# Exemplos SyntaxError
# a)
def funcao:
    print('Erro de Síntaxe')

# b)
None = 1

# c)
def = 1

# d)
return

2. NameError -> Ocorre quando uma variável ou função não foi definida

# Exemplos NameError
# a)
print(idade)

# b)
conta_pares()

3. TypeError -> Ocorre quando uma função/operação/ação é aplicada à um tipo errado

# Exemplos TypeError
# a)
print(len(5))

# b)
print('Paula' + [])

4. IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado
utilizando um índice inválido

# Exemplos IndexError
# a)
lista = ['Thiago']
print(lista[2])

# b)
lista = ['Thiago']
print(lista[0][6])

# c)
tupla = ('Thiago',)
print(tupla[2][30])

5. ValueError -> Ocorre quando uma função ou operação built-in (integrada) recebe um argumento com tipo
correto, mas valor inapropriado

# Exemplos ValueError
# a)
print(int('João'))

# b)
print(float('Paula'))

6. KeyError -> Ocorre quando tentamos acessar um dicionário com uma chave que não existe

# Exemplos KeyError
# a)
dicionario = {'python': 'language'}
print(dicionario['cpp'])

7. AttributeError -> Ocorre quando uma variável não tem um atributo ou função

# Exemplos AttributeError
# a)
tupla = (11, 2, 31, 4)
print(tupla.sort())

# b)
dicionario = {'a': 1, 'b': 2, 'c': 3}
print(dicionario.sort())

8. IndentationError -> Ocorre quando não respeitamos a indentação do Python

# Exemplos IndentantionError
# a)
def nova_funcao():
    print('Eu sou a nova função')

# b)
for i in range(10):
    i + 1


# OBS: Exception e Errors são sinônimos na programação
# OBS: Importante ler e prestar atenção na saída de erro
"""

# =============

"""
Levantando os próprios erros com Raise

raise -> Lança exceções

# OBS: O Raise não é uma função. É uma palavra reservada (keyword), assim como def, for, ou qualquer outra em Python

Para simplificar, pense no raise como sendo útil para que possamos criar nossas próprias exceções e mensagens de erro.
A forma geral de utilização é:
raise TipoDoErro('Mensagem de Erro')

# Exemplo Real
def colore(texto, cor):
    if not isinstance(texto, str):
        raise TypeError("Texto precisa ser uma string!")

    if not isinstance(cor, str):
        raise TypeError("Cor precisa ser uma string!")

    return f"O texto {texto} será impresso na cor {cor}"


print(colore(28, "azul"))

# Exemplo Refatorado
def colore(texto, cor):
    cores = ("verde", "amarelo", "azul", "branco")

    if not isinstance(texto, str):
        raise TypeError("Texto precisa ser uma string")

    if not isinstance(cor, str):
        raise TypeError("Cor precisa ser uma string!")

    if cor not in cores:
        raise ValueError(f"A cor precisa ser uma entre: {cores}")

    return f"O texto {texto} será impresso na cor {cor}"


print(colore("Hoje é meu aniversário", "amarelo"))

# OBS: O raise, assim como o return, finaliza a função. Ou seja, nada após o raise é executado.
"""

# =============

"""
O bloco try/except

Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso código. Previnindo assim que nosso programa
pare de funcionar e o usuário receba mensagens de erros inesperadas.

A forma geral mais simples é:
try:
    # Execução problemática
except:
    # O que deve ser feito em caso de problema


# Exemplo 1 - Tratando um erro genérico
# Tente executar a função soma_pares(), caso você encontre erros, imprima a mensagem de erro
try:
    soma_pares()
except:
    print('Deu algum problema')


# Exemplo 2 - Tratando erro genérico
# Tente executar a função len(5), caso você encontre erros, imprima a mensagem de erro
try:
    len(5)
except:
    print('Deu algum problema')


# Exemplo 3 - Tratando um NameError
try:
    soma_pares()
except NameError:
    print('Você está utilizando uma função inexistente!')


# Exemplo 4 - TypeError
try:
    len("Testando")
except TypeError:
    print('Você está utilizando um tipo de dado inválido!')


# Exemplo 5 - Tratando um TypeError com mensagem de erro detalhada
try:
    len()
except TypeError as error:
    print(f"A aplicação gerou o seguinte erro: {error}")


# Podemos efetuar diversos tratamentos de erros de uma vez
try:
    ().sort()
    # len()  # TypeError
    # soma_pares()  # NameError
    # print('Curso'[9])  # IndexError
except TypeError as typeErrorMessage:
    print(f"Deu TypeError: {typeErrorMessage}")
except NameError as nameErrorMessage:
    print(f"Deu NameError: {nameErrorMessage}")
except IndexError as indexErrorMessage:
    print(f"Deu IndexError: {indexErrorMessage}")
except:
    print("Deu um erro diferente")


# Podemos usar o bloco try/except dentro de funções
def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError as keyErrorMessage:
        return f'Chave inexistente: {keyErrorMessage}'
    except TypeError as typeErrorMessage:
        return f'Erro de tipo de dado: {typeErrorMessage}'

dicionario = {'nome': 'João'}
print(pega_valor(dicionario, 'idade'))
"""

# =============

"""
Try / Except / Else / Finally

Dica de quando e onde tratar código:
TODO INPUT DEVE SER TRATADO!

# OBS: A função do usuário é DESTRUIR o seu sistema

# Else -> É executado somente se não ocorrer o erro
try:
    num = int(input('Informe um número: '))
except ValueError as valueErrorMessage:
    print(f'Valor incorreto: {valueErrorMessage}')
else:
    print(f'Você digitou {num}')


# Finally -> É SEMPRE executado
try:
    num = int(input('Informe um número: '))
except ValueError as valueErrorMessage:
    print(f'Valor incorreto: {valueErrorMessage}')
else:
    print(f'Você digitou {num}')
finally:
    print('Executando o finally!')

# OBS: O bloco finally é geralmente utilizado para fechar ou desalocar recursos

# Exemplos mais complexo - ERRADO
def dividir(x, y):
    return x / y

try:
    num1 = int(input('Informe o primeiro número: '))
    num2 = int(input('Informe o segundo número: '))
except ValueError as valueErrorMsg:
    print('O valor precisa ser númerico!')
else:
    print(dividir(num1, num2))


# Exemplos mais complexo - CERTO
def dividir(x, y):
    try:
        return int(x) / int(y)
    except ValueError:
        return 'Valor incorreto'
    except ZeroDivisionError:
        return 'Não é possível dividir por zero!'

num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')
print(dividir(num1, num2))


# Exemplos mais complexo - Genérico
def dividir(x, y):
    try:
        return int(x) / int(y)
    except:
        return 'Ocorreu um erro'

num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')
print(dividir(num1, num2))

# Exemplos mais complexo - Semi-genérico
def dividir(x, y):
    try:
        return int(x) / int(y)
    except (ValueError, ZeroDivisionError) as error:
        return f"Ocorreu um erro: {error}"


num1 = input("Informe o primeiro número: ")
num2 = input("Informe o segundo número: ")
print(dividir(num1, num2))
"""

# =============

"""
Debuggando com PDB

PDB -> Python Debugger

Vida de Inseto -> Life's Bug

Bug -> Inseto


# OBS: A utilização do print() para debugar código é considerado uma prática ruim
def dividir(x, y):
    print(f"X = {x} ---- Y = {y}")
    try:
        return int(x) / int(y)
    except (ValueError, ZeroDivisionError) as error:
        return f"Ocorreu um erro: {error}"


print(dividir(4, "k"))

# Existem formais mais profissionais de se fazer esse debug. Utilizando o debugger
# em Python podemos fazer isso em diferentes IDEs, como o PyCharm, o VSCode, o VIM
# ou utilizando o PDB - Python Debugger

# Exemplo com o VSCode
def dividir(x, y):
    try:
        return int(x) / int(y)
    except (ValueError, ZeroDivisionError) as error:
        return f"Ocorreu um erro: {error}"


print(dividir(4, 0))

# Exemplo com o PDB - Python Debugger - Exemplo 1
# Para utilizar o Python Debugger, precisamos utilizar a função set_trace()

# Comandos básicos do PDB
# l - Listar onde estamos no código
# n - Próxima linha
# p - Imprime variável
# c - Continua a execução - Finaliza o Debugging

nome = 'Angelina'
sobrenome = 'Jolie'
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python'
final = nome_completo + ' faz o curso ' + curso
print(final)

# Por que utilizar este formato?
# O Debug é utilziado durante o desenvolvimento. Costumamos realizar todos os imports
# de bibliotecas no inicio do arquivo. Por isso, ao invés de colocarmos o import do PDB
# no início do arquivo, nós colocamos somente onde vamos debuggar, e ao finalizar já fazemos
# a remoção.

# Exemplo com o PDB - Python Debugger - Exemplo 2

# * A partir Python 3.7, não é mais necessário importar a biblioteca PDB, pois o comando de
# debug foi incorporado como função built-in (integrada) chamada breakpoint()


# OBS: Cuidado com conflitos entre nomes de variáveis e comandos do PDB
def soma(l, n, p, c):
    breakpoint()
    return l + n + p + c


print(soma(1, 3, 5, 7))

# Como os nomes da variáveis são os mesmos dos comandos do PDB, devemos utilizar o comando p
# para imprimir as variáveis. Ou seja: p nome_da_variável


# Nada de colocar nomes não representativos em variáveis. Sempre optar por nomes significativos
def soma(num1, num2, num3, num4):
    breakpoint()
    return num1 + num2 + num3 + num4
"""
