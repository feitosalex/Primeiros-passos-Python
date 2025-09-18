# #atividade 01
# atual = input ('Qual a sua idade atual?')
# sonho = input ('Qual a sua idade dos sonhos?')
# print (atual > sonho)
# print (atual < sonho)
# print (atual == sonho)

# #atividade 02
# marca1 = input ( 'qual a sua marca de tenis favorita?')
# marca2 = input ('Qual a sua marca de boné favorita?')
# print (marca1 == marca2)

# #atividade 03
# idade = input ('Digite sua idade')
# idade = float (idade)
# cnh = input ('Você possui CNH?')
# print (idade >= 18)
# print ('Possui CNH?') 
# print (cnh)
       
# # #atividade 04 forma1
# nota1 = input('Nota 1° semestre:')
# nota1 = float (nota1)
# nota2 = input('Nota 2° semestre:')
# nota2 = float (nota2)
# print (nota1 >= 6)
# print (nota2 >= 6)

# #forma2
# nota1 =float (input('Nota 1° semestre:'))
# nota2 =float (input('Nota 2° semestre:'))
# resultado=nota1 >= 6 and nota2 >= 6
# print('As duas notas são maiores ou iguais a 6?')
# print(resultado)

# #atividade 05
# preco = input ('Digite aqui o preço do produto:')
# preco= float(preco)
# print ('Preço do produto com desconto:')
# print (preco * 0.95)

# #atividade06
# numero = float (input('Quantos projetos para entregar essa semana?'))
# numero *= 2
# print (numero)

# #atividade07
# frase = input('Insira o nome da sua rua:')
# letra = input('Insira sua letra favorita:')
# resultado = letra in (frase)
# print (resultado)

# #atividade08
# frase= input('Digite uma frase que sua mãe sempre diz:')
# palavra=input('Digite uma palavra que sua mãe sempre diz:')
# resultado= palavra in frase
# print(resultado)

# #atividade 09
# numero = int(input('Digite seu número da sorte:'))
# if numero % 2 == 0:
#  print('O numero é par')
# else:
#  print('O número é impar')

# #atividade10
# nota=float(input('Insira a nota do aluno:'))
# if nota >= 6:
#     print('Aprovado')
# else:
#     print('Reprovado')

# #atividade11
# numero =float(input('Escolha um numero de sua preferência:'))
# if numero %2 == 0:
#     print('O número é par.')
# else:
#     print('O número é impar.')
# if numero >= 0:
#         print('O número é positivo.')
# else:
#      print('O número é negativo.')

# #atividade12
# peso=float(input('Quantos kilos você pesa?'))
# altura=float(input('Qual a sua altura?'))
# imc= peso/ (altura*altura)
# print(imc)
# if imc<18.5:
#  print('Abaixo do peso')
# elif imc <25:
#  print('Peso normal')
# elif imc <30:
#  print('Sobrepeso')
# else: 
#  print('Obesidade')

# #atividade13
# login=str(input('Login:'))
# senha=float(input('Senha:'))
# if login== 'admin' and senha==1234:
#     print('Acesso liberado')
# else:
#     print('Acesso negado')    
 
# #atividade14
# preco= float(input('Insira o preço unitário:R$'))
# quantidade=int(input('Quantas unidades?'))
# total= preco*quantidade
# print('Total')
# print(total)
# if quantidade>10:
#     print('Total com desconto:')
#     print (total*0.9)


# #repetindo a anterior sem ver depois de um tempo
# preco=float(input('Digite o valor do produto:R$:'))
# quantidade=int(input('Quantos(as):'))
# descontado= preco*quantidade
# if quantidade>10:
#     print(f'O preço com desconto é:{descontado*0.9}')

#REFAZENDO
#atividade01 Comparação de Idades:
# Peça ao usuário duas idades e use operadores de comparação para verificar se a primeira idade é maior, menor ou igual à segunda.
# idade1=int(input('Digite sua idade:'))
# idade2=int(input('Digite sua idade dos sonhos:'))
# if idade1>idade2:
#     print(f'{idade1} maior que {idade2}')
# elif idade1<idade2:
#     print(f'{idade1} menor que {idade2}')
# else:
#     print(f'{idade1} igual á {idade2}')

#atividade2 Verificar Igualdade de Strings:
# Peça ao usuário duas palavras e use operadores de comparação para verificar se elas são iguais.
# palavra1=input('Digite uma palavra:')
# palavra2=input('Digite mais uma palavra:')
# if palavra1==palavra2:
#     print('São iguais')
# else:
#     print('São diferentes')

#atividade03 Verificação de Maioridade e Habilitação:
# Crie um programa que peça a idade do usuário e se ele possui habilitação
# (sim ou não). Use operadores lógicos para verificar se ele é maior de idade (>= 18) e possui habilitação.
# idade=int(input('Digite sua idade:'))
# cnh=input('Você possui habilitação?:')
# if idade>17:
#     print('Maior de idade')
# else:
#     print('Menor de idade')
# print(f'Possui habilitação? {cnh}')

#atividade04 Verificação de Notas Aprovadas:
# Escreva um programa que peça duas notas de um aluno. Use operadores lógicos para verificar se as duas notas são maiores ou iguais a 6.
# nota1=float(input('Digite sua nota:'))
# nota2=float(input('Digite sua nota:'))
# if nota1>=6 and nota2>=6:
#     print('As duas notas são maiores ou iguais a 6.')
# else:
#     print('Uma ou todas as notas são menores que 6')

#atividade05 Desconto em Preço:
#Peça ao usuário para inserir o preço de um produto e, em seguida,use o operador de atribuição -= para aplicar um desconto de 5%.
# preco=float(input('Insira o preço:'))
# preco *= 0.05
# print(preco)

#atividade06 Dobro do Valor:
#Solicite ao usuário um número e use o operador de atribuição *= para dobrar o valor e exibir o resultado.
# numero=float(input('Insira um número:'))
# numero*=2
# print(numero)

#atividade07 Verificação de Caracteres em uma String:
# Crie um programa que peça ao usuário uma frase e um caractere.
# Use o operador de associação in para verificar se o caractere estápresente na frase.
# frase=input('Digite uma frase:')
# caracter=input('Digite um caracter:')
# if caracter in frase:
#     print('O caracter está na frase')
# else:
#     print('O caracter não está na frase')

#atividade08 Verificação de Palavras em uma Frase:
#Peça ao usuário para inserir uma frase e uma palavra. Use in para verificar se a palavra está na frase.
# frase=input('Insira uma frase:')
# palavra=input('Insira uma palavra')
# if palavra in frase:
#     print('A palavra está na frase:')
# else:
#     print('A palavra não está na frase')

#atividade09 Verificar Par ou Ímpar:
#Crie um programa que peça ao usuário um número e use a estrutura condicional if para verificar se ele é par ou ímpar.
# numero=int(input('Insira um numero:'))
# if numero%2==0:
#     print('O número é par')
# else:
#     print('O número é impar')

#atividede10 Verificar Nota para Aprovado:
#Crie um programa que peça a nota de um aluno e use if para verificar se ele foi aprovado (nota >= 6).
# nota=float(input('Digite sua nota:'))
# if nota>=6:
#     print('O aluno foi aprovado!')
# else:
#     print('O aluno foi reprovado')

#atividade11 Verificar Par ou Ímpar e Positivo ou Negativo:
#Escreva um programa que peça um número e use if para verificar se ele é par ou ímpar e também se é positivo ou negativo.
# numero=int(input('Insira um número:'))
# if numero%2==0:
#     print('O número é par')
# else:
#     print('O número é impar')
# if numero>0:
#     print('O número é positivo')
# elif numero==0:
#     print('0 é número neutro')
# else:
#     print('O numero é negativo')

#atividade12Verificar Classificação de IMC:
#Crie um programa que calcule o Índice de Massa Corporal (IMC) e use if para classificar o resultado em "Abaixo do peso"
#"Peso normal""Sobrepeso" e "Obesidade".
# peso=float(input('Digite seu peso:'))
# altura=float(input('Digite sua idade em metros:'))
# imc=peso/altura**2
# if imc<=18.5:
#     print(imc)
#     print('Abaixo do peso')
# elif 18.5< imc < 25:
#     print(imc)
#     print('Peso normal')
# elif 25 < imc < 30:
#     print(imc)
#     print('Sobrepeso')
# else:
#     print(imc)
#     print('Obeso')

#atividade13 Sistema de Login Simples:
# Desenvolva um programa que peça ao usuário um nome de usuário
# e uma senha e use if para verificar se são iguais a "admin" e "1234",respectivamente.
# login=input('Digite seu login:')
# senha=input('Insira sua senha:')
# if login=='admin' and senha=='1234':
#     print('Acesso liberado')
# else:
#     print('Senha incorreta')

# atividade14 Verificar Status de Taxa de Desconto:
# Crie um programa que peça ao usuário o preço original de um produto e a quantidade comprada. Use if para verificar se a quantidade é 
# maior que 10 para aplicar um desconto de 10% sobre o total.
# preco=float(input('Preço:'))
# quantidade=int(input('Quantidade:'))
# total=preco*quantidade
# if quantidade>10:
#     total=total*0.90
#     print(f'Valor com desconto:R${total}')
# else:
#     print(f'Valor insuficiente para desconto:R${total}')
