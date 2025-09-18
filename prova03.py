#PROVA03 

# Você está criando um programa em Python para simular um jogo simples de adivinhação. O programa deve ter um número fixo, 
# por exemplo, 7, que o jogador deve adivinhar. O jogador terá até 3 tentativas para acertar o número.
# Implemente o jogo utilizando um loop while para permitir que o jogador faça múltiplas tentativas até acertar ou atingir
# o limite de tentativas. Utilize a estrutura else para exibir uma mensagem de encorajamento caso o jogador acerte 
# e uma mensagem de consolo caso as 3 tentativas se esgotem sem sucesso.

senha=8
jogadas=0
tentativas=3
while jogadas<tentativas:
    palpite=int(input('Advinhe a senha:'))
    jogadas+=1
    if palpite==senha:
        print('Parabens você venceu o desafio!!')
        break
else:
    print('Você foi muito corajoso!! Jogue novamente, sei que vai acertar:)')









