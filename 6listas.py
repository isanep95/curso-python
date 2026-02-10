# Listas e Tuplas

# Tipos de dados que armazenam múltiplos valores, mas têm diferenças importantes:

# Listas:
# - Modificável (pode adicionar, remover e alterar valores)
# - Mais lenta
# - Quando precisamos modificar dados

# Tuplas:
# - Não é modificável (uma vez criada, não pode ser alterada)
# - Mais rápida
# - Quando os dados não devem ser alterados
# Lista
# Definida entre colchetes [] e pode armazenar diferentes tipos de dados

# frutas = ["maçã", "banana", "laranja"]
# números = [1, 2, 3, 4, 5]
# mista = ["texto", 42, 3.14, True]

# Acessando elementos da lista
#print(frutas[0])  # Saída: maçã
#print(números[2])  # Saída: 3
#print(mista[1])  # Saída: 42

# Alterando um valor na lista

#frutas[1] = "uva"
#print(frutas)  # Saída: ['maçã', 'uva', 'laranja']

# Adicionando elementos à lista
# append(): adiciona um item ao final
# insert(): adiciona um item em uma posição específica

# numeros = [1, 2, 3]
# numeros.append(4)
# print(numeros)  # Saída: [1, 2, 3, 4]

# numeros.insert(1, 10) # (posição, valor)
# print(numeros)  # Saída: [1, 10, 2, 3, 4] (inseriu o 10 na posição 1)

# Removendo elementos da lista
# remove(): remove um item pelo valor
# pop(): remove um item pelo índice (ou o último item se nenhum índice for passado)

# frutas = ["maçã", "banana", "laranja"]
# frutas.remove("banana")
# print(frutas)  # Saída: ['maçã', 'laranja']

# frutas.pop(0)  # Remove o item na posição 0 (maçã)
# print(frutas)  # Saída: ['laranja']

# Tupla
# Tuplas são como listas, mas imutáveis. Elas são criadas com parênteses ().

cores = ("vermelho", "verde", "azul")
numeros = (1, 2, 3, 4, 5)

# Acessando elementos
# print(cores[0])  # Saída: "vermelho"
# print(cores[-1])  # Saída: "verde"

# Tentando modificar uma tupla (Erro!)
# cores[1] = "amarelo"  # Isso vai gerar um erro, pois tuplas são imutáveis!

# Convertendo entre lista e tupla
# Podemos converter uma tupla para uma lista e modificar os elementos.

# tupla = (1, 2, 3)
# lista = list(tupla) # Converte para lista
# lista.append(4)  # Modifica a lista
# tupla = tuple(lista) # Converte de volta para tupla
# print(tupla)  # Saída: (1, 2, 3, 4)

# Quando usar tupla?

# - Quando queremos garantir que os valores não sejam alterados.
# - Para armazenar dados fixos como coordenadas, meses do ano, dias da semana, etc.

meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",)
print(meses[2]) #"Março"
