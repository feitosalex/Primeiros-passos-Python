# EXERCICIOS DE FOR
# EXERCICIO MAIS INTERESSANTE: ATIVIDADE 09
#Atividade01 Tabuada de um Número:
# Faça um programa que solicite um número ao usuário e use um laço for para exibir a tabuada desse número (de 1 a 10).
# numero=float(input('Insira um número:'))
# for multiplica in range(1,10):
#     resultado=numero*multiplica
#     print(f'{numero}x{multiplica}={resultado}')
#     multiplica+=1

#atividade02 Soma de Números de 1 a 100:
# Crie um programa que use um laço for para somar todos os números de 1 a 100 e exiba o resultado.
# soma=0
# for numero in range(1,100):
#     numero+=1
#     soma+=numero
# print(soma)

#atividade03 Caractere por Caractere:
# Escreva um programa que solicite uma palavra ao usuário e use um laço for para exibir cada caractere da palavra em uma linha separada.

# palavra=input('Digite uma palavra:')
# for caractere in palavra:
#     print(caractere)

#Atividade04 Contagem Regressiva de 10 a 1:
# Desenvolva um programa que use um laço for para fazer uma contagem regressiva de 10 até 1 e, em seguida, exiba "Feliz Ano Novo!".
# numero=10
# for i in range (0,10):
#     print(numero)
#     # numero-=1
#     numero=numero-1
# print('Feliz ano novo!!')

#Atividade05 Contagem de Números Positivos e Negativos:
# Escreva um programa que solicite ao usuário 10 números e use um
# laço for com uma condicional para contar quantos são positivos e quantos são negativos.
# contador_negativo=0
# contador_positivo=0
# for n in range(1,11):
#     numero=int(input(f'Digite o {n}º número: '))
#     if numero>0:
#         contador_positivo+=1
#     elif numero<0:
#         contador_negativo+=1
# print(f'Temos {contador_positivo} numeros positivos e {contador_negativo} números negativos')

# Atividade 07:
# Contagem de Vogais em uma Palavra: Crie um programa que solicite uma palavra ao usuário e use um laço for com
# uma condicional para contar quantas vogais (a, e, i, o, u) a palavra contém.
# palavra=input('Digite uma palavra: ')
# qtd=0
# for letra in palavra:
#     if letra in 'aeiou':
#         qtd+=1
# print('Temos',qtd ,'vogais')

# Atividade 08:
# Cálculo de Média de Notas:
# Escreva um programa que solicite 5 notas de alunos. Use um laço for
# para somar as notas e uma condicional para exibir a média e a
# classificação ("Aprovado" para média >= 6,
# "Reprovado" para média < 6).
# somador=0
# for nota in range (1,6):
#     notas=float(input(f'Digite a {nota}ª nota: '))
#     somador+=notas
#     media=somador/5
# if media>=6:
#     print(f'Aprovado \nMédia={media}')
# else:
#     print(f'Reprovado \nMédia={media}')

# Atividade 09:
# Soma de Números com Desconto:
# Peça ao usuário para inserir 5 preços de produtos. Use um laço for para
# calcular o total. Aplique um desconto de 10% se o total ultrapassar 100 e
# interrompa o loop com break.
# total=0
# for p in range(1,6):
#     preco=float(input(f'{p}º preço: R$'))
#     total+=preco
#     if total>100:
#         break
# print(total*0.9)        