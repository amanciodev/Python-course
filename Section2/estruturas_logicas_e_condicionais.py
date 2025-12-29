"""
Estruturas Condicionais

if (Se)
elif (Senão se)
else (Senão)

idade = int(input('Digite a sua idade: '))

if idade < 18:
    print('Menor de idade')
elif idade == 18:
    print('Tem 18 anos')
else:
    print('Maior de idade')

# Também podemos fazer assim, mas dependendo do seu programa, o resultado poderá ser diferente
if idade < 18:
    print('Menor de idade')

if idade == 18:
    print('Tem 18 anos')

if idade == 26:
    print('Tem 26 anos')

if idade > 18:
    print('Maior de idade')
"""

# ===============================

"""
Estruturas Lógicas: and (e), or (ou), is (é)

Operadores unários:
    - not, is

Operadores binários:
    - and, or

# Para o 'and', ambos os valores precisam ser True
# Para o 'or', um ou outro valor precisa ser True
# Para o 'not', o valor do booleano é invertido, ou seja, se for True, vira False, se for False vira True

ativo = False
logado = False

if ativo or logado:
    print('Bem-vindo usuário')
else:
    print('Você precisa ativar a sua conta. Por favor, verifique o seu e-mail')


if ativo and logado:
    print('Bem-vindo usuário')
else:
    print('Você precisa ativar a sua conta. Por favor, verifique o seu e-mail')


if not ativo:
    print('Você precisa ativar a sua conta. Por favor, verifique o seu e-mail')
else:
    print('Bem-vindo usuário')
"""
