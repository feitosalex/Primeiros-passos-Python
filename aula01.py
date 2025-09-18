# atividade 01
saudacao = print('Hello World')

# atividade 02
nome =input('Nome completo:')
print(nome)
type(str)

idade = input('Qual a sua idade:')
print(idade)
type(int)

altura = input('Qual a sua altura:')
print(altura)
type(float)


# atividade03
nota1 = input('Nota 1° bimestre:')
nota2 = input('Nota 2° bimestre:')
nota3 = input('Nota 3° bimestre:')
nota4 = input('Nota 4° bimestre:')
nota1 = float(nota1)
nota2 =float(nota2)
nota3 =float(nota3)
nota4 =float(nota4)
media =((nota1+nota2+nota3+nota4)/4)
print(f'A média é:{media}')

#atividade04
salario = input('Valor do salário mensal:')
salario = float(salario)

horas = input('Quantas horas você trabalha por semana?')
horas = float(horas)

horasmes = (horas*4)
valorhora = (salario/horasmes)
print(f'O valor da hora trabalhada é de:{valorhora}')

#atividade05
nome = input('Digite seu nome:')
idade = input('Qual a sua idade?')
idade = int(idade)
cidade = input('Qual cidade você nasceu?')

print(f'Nome:{nome} Idade:{idade} Cidade:{cidade}')