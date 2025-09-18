#ATIVIDADE01
# Conversão de Unidades: Crie um programa que converta metros para centímetros.
# Peça ao usuário para digitar um valor em metros, armazene em uma variável e converta para centímetros.
# metros=float(input('Insira sua altura em metros:'))
# cm=metros*100
# print(f'Sua altura em centimetros é:{cm}cm')

#ATIVIDADE02
# Cálculo de Área: Crie um programa que calcule a área de um retângulo.
# Peça ao usuário para digitar a largura e a altura, armazene em variáveis e calcule a área.
# altura=int(input('Digite a altura do retângulo:'))
# largura=int(input('Digite a largura do retângulo:'))
# area=altura*largura
# print(f'A área é igual a {area}')

#ATIVIDADE03
# Cálculo de IMC: Crie um programa que calcule o Índice de Massa Corporal (IMC).
# Peça ao usuário para digitar seu peso e altura, armazene em variáveis e calcule o IMC.
# peso=float(input('Digite seu peso:'))
# altura=float(input('Digite sua altura:'))
# altura=altura*altura
# imc=peso/altura
# print(f'Seu imc é de {imc}')

#ATIVIDADE04
# Cálculo de Juros Simples: Crie um programa que calcule o valor futuro de um investimento
# usando a fórmula de juros simples. Peça ao usuário para digitar o capital inicial, a taxa de juros e o tempo de aplicação.
# capital=int(input('Insira o valor de aporte inicial:R$'))
# taxa=int(input('Insira a taxa de juros da aplicação:'))
# tempo=int(input('Por quanto tempo ficará aplicado?:'))
# taxa= taxa/100
# total=capital*taxa*tempo
# total+=capital
# print(f'O valor total no final do exercício é de R${total}')

#ATIVIDADE05
# Verificando a Média do Aluno:
# Crie um algoritmo que peça quatro notas de um aluno, calcule a média e exiba se o aluno foi aprovado ou reprovado (média >= 6).
# nota1=float(input('Insira sua primeira nota:'))
# nota2=float(input('Insira sua segunda nota:'))
# nota3=float(input('Insira sua terceira nota:'))
# nota4=float(input('Insira sua quarta nota:'))
# soma= nota1+nota2+nota3+nota4
# media=soma/4
# if media>=6:
#     print(f'Média:{media}.Aprovado!')
# else:
#     print(f'Média:{media}Reprovado!')

#ATIVIDADE06
# Algoritmo de Cálculo de Desconto:Desenvolva um algoritmo que calcule o preço de um produto
# após aplicar um desconto. Solicite o preço original e o percentual de desconto.
# preco=float(input('Digite o preco do produto:R$'))
# desconto=int(input('Digite o percentual de desconto:'))
# desconto=desconto/100
# valor_desconto=preco*desconto
# total=preco-valor_desconto
# print(f'O valor com desconto é:R${total}')

#ATIVIDADE07
# Algoritmo de Conversão de Tempo:
# Desenvolva um algoritmo que converta uma quantidade de segundos fornecida pelo usuário em horas, minutos e segundos.
# segundo=int(input('Insira quantos segundos quiser:'))
# horas=segundo//3600
# resto=segundo%3600
# minutos=resto//60
# segundos=resto%60
# print(f'{segundo} segundos equivalem a {horas}h, {minutos}min, e {segundos}s')

#ATIVIDADE08
# Algoritmo de Conversão de Temperatura: Crie um algoritmo que converta uma temperatura de Celsius
# para Fahrenheit. Solicite ao usuário a temperatura em Celsius e exiba o resultado em Fahrenheit.
# graus=int(input('Insira quantos graus estão fazendo na sua cidade:'))
# fh=graus*1.8+32
# print(f'{graus}°C correspondem a {fh}F')

#ATIVIDADE09
# Categoria de Idade:
# Desenvolva um programa que peça a idade do usuário e informe se ele é criança, adolescente, adulto ou idoso.
# idade=int(input('Digite sua idade:'))
# if idade<=12:
#     print('Você é uma criança')
# elif idade<=18:
#     print('Você é um adolescente')
# elif idade<=59:
#     print('Você é um adulto')
# else:
#     print('Você é um idoso')

#ATIVIDADE10
# Classificação de Notas:
# Crie um programa que solicite uma nota de 0 a 100 e informe o conceito (A, B, C, D, F) com base na nota.
# nota=int(input('Insira sua nota anual:'))
# if nota>=80:
#     print('A')
# elif nota>=70:
#     print('B')
# elif nota>=60:
#     print('C')
# elif nota>=50:
#     print('D')
# else:
#     print('F')

#ATIVIDADE11
# Verificar Signo:
# Escreva um programa que peça o dia e o mês de nascimento do usuário e informe o signo correspondente.
# dia=int(input('Digite o dia que nasceu:'))
# mes=int(input('Digite o número equivalente ao mês que nasceu:'))
# if (dia>=21 and mes==3) or (dia<=20 and mes==4):
#     print('Áries')
# elif dia>=21 and mes==4 or dia<=20 and mes==5:
#     print('Touro')
# elif dia>=21 and mes==5 or dia<=20 and mes==6:
#     print('Gêmeos')
# elif dia>=21 and mes==6 or dia<=22 and mes==7:
#     print('Cancêr')
# elif dia>=23 and mes==7 or dia<=22 and mes==8:
#     print('Leão')
# elif dia>=23 and mes==8 or dia<=22 and mes==9:
#     print('Virgem')
# elif dia>=23  and mes==9 or dia<=22 and mes==10:
#     print('Libra')
# elif dia>=23 and mes==10 or dia<=21 and mes==11:
#     print('Escorpião')
# elif dia>=22 and mes==11 or dia<=21 and mes==12:
#     print('Sagitário')
# elif dia>=22 and mes==12 or dia<=20 and mes==1:
#     print('Capricornio')
# elif dia>=21  and mes==1 or dia<=18 and mes==2:
#     print('Aquario')
# elif (dia>=19  and mes==2) or (dia<=20 and mes==3):
#     print('Peixes')
# else:
#     ('Mês de São Nunca')

#ATIVIDADE12
# Sistema de Login:
# Desenvolva um programa que simule um sistema de login. O programa deve pedir o nome de usuário e a senha e verificar
# se correspondem a um usuário pré-cadastrado. Exiba mensagens apropriadas para login bem-sucedido ou falha.
# login=input('Crie seu login:')
# senha=input('Crie uma senha forte:')
# while True:
#     tentativa_login=input('Digite seu login:')
#     tentativa_senha=input('Digite sua senha:')
#     if tentativa_login==login and tentativa_senha==senha:
#         print('Acesso concedido!')
#         break
#     elif tentativa_senha!=senha and tentativa_login== login:
#         print('Senha incorreta')
#     elif tentativa_login!=login and tentativa_senha==senha:
#         print('Login incorreto')
#     else:
#         print('Caso não tenha uma conta crie já a sua.')

#ATIVIDADE13
# Contagem Regressiva:
# Desenvolva um programa que use um laço while para exibir uma contagem regressiva de 10 até 1 e, em seguida, exiba "Feliz Ano Novo!".
# numero=10
# while numero>0:
#     print(numero)
#     numero-=1
# print('Feliz ano novo')

#ATIVIDADE14
# Contagem Regressiva:
# Desenvolva um programa que use um laço for para exibir uma contagem regressiva de 10 até 1 e, em seguida, exiba "Feliz Ano Novo!".
# numero=10
# for numero in range(10,0,-1):
#     print(numero)
# print('Feliz ano novo')

#ATIVIDADE15
# Soma de Números Pares:
# Crie um programa que use um laço while para somar todos os números pares de 1 a 100 e exiba o resultado.
# numero=1
# soma=0
# while numero<=100:
#     numero+=1
#     if numero%2==0:
#         soma+=numero
# print(soma)

#ATIVIDADE16
# Tabuada de um Número:
# Faça um programa que solicite um número ao usuário e use um laço for para exibir a tabuada desse número (de 1 a 10).
# numero=int(input('Digite um número qualquer:'))
# multiplica=1
# for multiplica in range (1,11):
#     resultado=numero*multiplica
#     print(f'{numero}x{multiplica}={resultado}')

#ATIVIDADE17
# Verificação de Palíndromo:
# Escreva um programa que solicite uma palavra ao usuário e
# use um laço while para verificar se a palavra é um palíndromo (lê-se da mesma forma de trás para frente).
# palavra=input('Digite uma palavra:').lower()
# inicio=0
# fim=len(palavra) -1
# palindromo=True
# while inicio<fim:
#     if palavra[inicio] != palavra[fim]:
#         palindromo=False
#         break
#     inicio+=1
#     fim-=1
# if palindromo==True:
#     print('A palavra é um palíndromo')
# else:
#     print('A palavra não é um palíndromo')

#ATIVIDADE18
# Sistema de Login com Tentativas Limitadas:
# Desenvolva um programa que simule um sistema de login. O programa deve solicitar o nome de usuário e senha até que o
# usuário insira as credenciais corretas ou até que o número máximo de tentativas seja atingido. Use um laço while com uma condicional
# para verificar as credenciais e limitar as tentativas.
# login=input('Crie um login:')
# senha=input('Crie sua senha:')
# tentativas=0
# while tentativas<3:
#     tentativa_login=input('Digite seu login:')
#     tentativa_senha=input('Digite sua senha:')
#     if tentativa_login!=login or tentativa_senha!=senha:
#         tentativas+=1
#         print('Senha ou login não conferem.')
#     else:
#         print('Acesso liberado')
#         break