
#Atividade01:Contagem de 1 a 10:
#Crie um programa que use um laço while para contar de 1 a 10 e exibir cada número.
# numero=0
# while numero<10:
#     numero+=1
#     print(numero)

#Atividade02:Soma de Números de 1 a 100:
#Escreva um programa que use um laço while para somar os números de 1 a 100 e exiba o resultado.
# numero=0
# soma=0
# while numero<=100:
#     numero+=1
#     soma+=numero
# print(soma)

#atividade03 Tabuada de um Número:
#Faça um programa que solicite um número ao usuário e use um laço while para exibir a tabuada desse número (de 1 a 10).
# numero=int(input('Digite sua data de aniversário:'))
# multiplica=0
# while multiplica<10:
#     multiplica+=1
#     resultado= multiplica*numero
#     print(f'{numero}x{multiplica}={resultado}')

#atividade04 Contagem Regressiva:
# Desenvolva um programa que use um laço while para exibir uma contagem regressiva de 10 até 1 e, em seguida, exiba "Feliz Ano Novo!".
# numero=11
# while numero>=2:
#     numero-=1
#     print(numero)
# print('Feliz ano novo!!')

#atividade05 Contagem até o Número Inserido:
# Crie um programa que solicite um número ao usuário e use um laço while para contar de 1 até o número inserido, exibindo apenas os números ímpares.
# numero=float(input('Insira um numero:'))
# contador=0
# while contador<numero:
#     contador+=1
#     if contador%2!=0:
#         print(contador)

#atividade06 Soma de Números Positivos:
#Escreva um programa que solicite números ao usuário até que ele digite um número negativo, somando apenas os números positivos inseridos.
# soma=0
# while True:
#     numero=int(input('Digite numeros:'))
#     soma+=numero
#     if numero<0:
#         break
#     print(soma)

#atividade07 Tabuada com Condicional:
# Faça um programa que solicite um número ao usuário e use um laço while para exibir a tabuada desse número (de 1 a 10),
# mas apenas para os resultados que forem múltiplos de 3.
# numero=float(input('Insira seu número da sorte:'))
# multiplica=0
# while multiplica<=10:
#     multiplica+=1
#     resultado=multiplica*numero
#     if resultado%3==0:
#         print(f'{numero}x{multiplica}={resultado})

#atividade08 Média de Notas:
# Desenvolva um programa que solicite as notas dos alunos até que o usuário digite -1. Calcule e exiba a média das notas inseridas.
# quantidade=0
# soma=0
# while True:
#     nota=float(input('Digite suas notas:'))
#     if nota==-1:
#         break
#     quantidade+=1
#     soma+=nota
#     resultado=soma/quantidade
# print(resultado)

#atividade09 Contagem até 10:
# Crie um programa que use um laço while para contar de 1 a 10 e termine quando atingir 10.
# numero=0
# while numero<=9:
#     numero+=1
#     print(numero)

#atividade10 Soma até 50:
#Escreva um programa que use um laço while para somar números consecutivos começando de 1 e termine quando a soma atingir ou ultrapassar 50.
# numero=0
# soma=0
# while soma<=50:
#     numero+=1
#     soma+=numero
#     print(soma)

#atividade11 Entrada Válida:
# Crie um programa que solicite ao usuário um número entre 1 e 10. Continue pedindo até que o usuário forneça um valor válido.
# while True:
#     numero=int(input('Insira um numero entre 1 e 10:'))
#     if 0<numero<11:
#         break

#atividade12 Senha Correta:
# Desenvolva um programa que peça ao usuário para digitar uma senha e continue pedindo até que a senha correta (previamente definida) seja inserida.
# senha=input('Defina sua senha:')
# tentativa=input('Digite sua senha:')
# while True:
#     if senha!=tentativa:
#         tentativa=input('Digite sua senha:')
#     else:

#DESAFIOS
#01Soma de Números Pares:
# Crie um programa que use um laço while para somar todos os números pares de 1 a 100 e exiba o resultado.
# numero=0
# soma=0
# while numero<100:
#     numero+=1
#     soma+=numero
# if soma%2==0:
#     print(soma)

#02 Números Ímpares de 1 a 50:
#Escreva um programa que use um laço while para exibir todos os números ímpares de 1 a 50.
# numero=0
# while numero<50:
#     numero+=1
#     if numero%2!=0:
#         print(numero)

#03 Sequência de Fibonacci:
# Faça um programa que use um laço while para exibir os primeiros 20 termos da sequência de Fibonacci.(soma do atual e anterior)    
# inicio=0
# referencia=1
# quantidade=0
# print(inicio)
# while quantidade<=20:
#     print(referencia)
#     proximo=referencia+inicio
#     inicio=referencia
#     referencia=proximo
#     quantidade+=1

#04 Fatorial de um Número:
# Desenvolva um programa que solicite um número ao usuário e use um laço while para calcular o fatorial desse número.
# numero=int(input('Digite um número positivo:'))
# multilplicador=numero-1
# while multilplicador>0:
#     resultado=multilplicador*numero
#     print(f'{numero}x{multilplicador}= {resultado}')
#     numero=resultado
#     multilplicador-=1

#05 - Números Pares em um Intervalo:
# Crie um programa que solicite dois números ao usuário, representando um intervalo. Use um laço while para exibir
# todos os números pares dentro desse intervalo.
# minimo=int(input('Insira o valor minimo:'))
# maximo=int(input('Insita o valor máximo:'))
# numero=minimo+1
# if minimo>maximo:
#     print('O valor minimo precisar ser menor que o máximo, reinicie o programa e tente novamente!! Grato pela compreensão.')
# while numero<maximo:
#     if numero%2==0:
#         print(numero)
#     numero+=1

#06 Contagem Regressiva com Verificação:
# Faça um programa que use um laço while para fazer uma contagem regressiva de um número inserido pelo usuário até 0.
# Durante a contagem, exiba "Número par" para os números pares.
# numero=int(input('Insira um número:'))
# contador=numero
# while contador>=0:
#     print(contador)
#     if contador%2==0:
#         print('Numero par')
#     contador-=1


#07 Sequência de Collatz:
# Crie um programa que solicite um número ao usuário e use um
# laço while para gerar e exibir a sequência de Collatz até chegar ao número 1.
# numero=int(input('Digite um número:'))
# while True:
#     if numero==1:
#         break
#     elif numero%2==0:
#         numero=numero/2
#         print(numero)
#     elif numero%2!=0:
#         numero= numero*3 + 1
#         print(numero)

#08 Soma de Dígitos:
# Escreva um programa que solicite um número ao usuário e use
# um laço while para somar os dígitos do número até que a soma seja um único dígito.
# numero=int(input('Digite o ano que você nasceu:'))

#09 Adivinhar Número:
# Desenvolva um jogo de adivinhação onde o programa escolhe um número aleatório entre 1 e 100. O usuário deve tentar 
# adivinhar o número, e o programa deve fornecer dicas se o palpite está muito alto ou baixo.

    
    
    
    



    