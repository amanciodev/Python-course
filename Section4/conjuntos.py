"""
Conjuntos

- Conjuntos em qualquer linguaguem de programação, estamos fazendo referência à Teoria dos Conjuntos da Matemática
- Aqui em Python, os conjuntos são chamados de Sets

Dito isto, da mesma forma que na matemática:
- Sets (conjuntos) não possuem valores duplicados
- Sets (conjuntos) não possuem valores ordenados
- Elementos não são acessados via índice, ou seja, conjuntos não são indexados

# Conjuntos são bons para se utilizar quando precisamos armazenar elementos
# mas não nos importamos com a ordenação deles. Quando não precisamos se preocupar
# com chaves, valores e itens duplicados

# Os conjuntos (sets) são refenciados em Python com chaves {}
# Diferença entre Conjuntos (Sets) e Mapas (Dicionários) em Python:
    # - Um dicionário tem chave/valor;
    # - Um conjunto tem apenas valor

# Definindo um conjunto
# Forma 1 - MENOS COMUM
meu_conjunto = set({1, 2, 3, 4, 5, 6, 7, 2, 3})  # Repare que temos valores repetidos
print(meu_conjunto)
print(type(meu_conjunto))

# OBS: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo
# será ignorado sem gerar erros e não fará parte do conjunto
"""
# Forma 2 - MAIS COMUM
meu_conjunto = {1, 2, 3, 4, 5, 5}
print(meu_conjunto)
print(type(meu_conjunto))

# Método .add()
meu_conjunto.add(7)
print(meu_conjunto)

# Método .pop()
meu_conjunto.pop()
print(meu_conjunto)

# Método .clear()
meu_conjunto.clear()
print(meu_conjunto)

