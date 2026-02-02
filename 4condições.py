#Condicionais

#São estruturas que permitem ao nosso programa tomar decisões com base
#em condições específicas. Em outras palavras, o programa pode executar
#ações diferentes dependendo de uma situação específica.

#Exemplo:

#Você está em uma cafeteria e está com pouca grana.
#O cappuccino custa 10 reais, café com leite 7 e o café simples 4.

#Se você tiver 10 reais ou mais, pode comprar o cappuccino.
#Se tiver 7 reais ou mais, pode comprar o café com leite.
#Se não, pode comprar o café simples.



#Sintaxe básica no Python!

# if - "se"
# elif - "senão, se"
# else - "senão"

#if condição:
    #Código a ser executado se a condição for verdadeira
    #elif outra_condição:
        #Código executado se a primeira condição for falsa, mas essa for verdadeira
    #else:
        #Código executado se nenhuma das condições anteriores for verdadeira




# EXEMPLOS
# Verificando a idade para a entrada em um evento (18 ANOS)

#idade = int(input("Digite sua idade: ")) # Usuário digita a idade
#if idade >=18:
#    print("Você pode entrar no evento!")
#else:
#    print("Você não pode entrar no evento!")

# Verificando a nota de um aluno

nota = float(input("Digite a nota do aluno: ")) # Usuário digita a nota

if nota >= 7.0:
    print("Aluno aprovado!")
elif nota >= 5.0:
    print("Aluno em recuperação!")
else:
    print("Aluno reprovado!")