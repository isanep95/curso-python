# Laços de repetição (for e while)

# Imagine que você precisa pedir para alguém contar de 1 a 100
# e escrever cada número em um papel. Fazer isso manualmente
# seria muito cansativo, né?

# Agora, imagine que um programa pode fazer essa contagem automaticamente,
# sem precisar repetir o mesmo comando 100 vezes. É exatamente isso
# que os laços de repetição fazem!

# Os laços de repetição são usados para executar um bloco de código
# várias vezes, até que uma condição seja atingida.

# Python tem dois tipos principais de laços:
# for - Quando sabemos quantas vezes queremos repetir algo.
# while - Quando queremos repetir algo até que uma condição seja verdadeira.





# FOR
# O for é usado quando sabemos quantas vezes queremos repetir um bloco de código.
# Ele percorre uma sequência de valores, como uma lista, um intervalo de números
# ou até mesmo letras de uma palavra.

# Estrutura:

# for variável in sequência:
    # Código a ser repetido



    # Contando de 1 a 5 com FOR

# for numero in range(1, 6):
        # print(numero)
    # O range(1, 6) gera os números de 1 a 5, o último número do range não é incluído.
    # [1, 2, 3, 4, 5]

# Percorrendo uma lista de compras

compras = ["Arroz", "Feijão", "Macarrão", "Leite"]

for item in compras:
    print(f"Comprar {item}")
