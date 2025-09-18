# [LPIA-A06]  Crie um programa em Python que simule um sistema de login. 
# O programa deve permitir ao usuário três tentativas para acertar o nome de usuário e a senha corretos. 
# Caso o usuário erre as credenciais, o programa deve fornecer uma mensagem informando quantas tentativas restam. 
# Se o usuário acertar, uma mensagem de boas-vindas deve ser exibida, e o programa deve terminar imediatamente.

# Se todas as três tentativas falharem, 
# o programa deve usar um loop for para exibir uma mensagem de "Acesso bloqueado" repetida três vezes.

tentativas=3
login='soualunodainfinity'
senha='vaidacerto'
while tentativas>0:
    tentativa_login=input('Digite o login corretamente: ')
    tentativa_senha=input('Digite a senha corretamente: ')
    if login==tentativa_login and senha==tentativa_senha:
        print('Acesso concedido!')
        break
    elif tentativa_senha!=senha or tentativa_login!=login:
        tentativas-=1
        print(f'Senha ou login incorretos, restam {tentativas} tentativas')
for i in range(3):
    if tentativas==0:
        print('Acesso bloqueado')