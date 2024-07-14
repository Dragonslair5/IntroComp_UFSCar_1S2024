import random 


# Função que executa o Adivinha Numero
def jogo_de_adivinhar_numero():

    numero_de_jogadores = int(input("Quantos jogadores? "))
    placar = []

    i = 0
    while i < numero_de_jogadores:
        i = i + 1
        nome = input("Qual seu nome? ")
        numero_secreto = random.randint(1,10)

        tentativas = 1
        acertou = False
        while not acertou:
            palpite = int(input("Adivinhe um numero de 1 a 10: "))
            if palpite == numero_secreto:
                print("Acertou! Parabéns!")
                acertou = True
            else:
                print("Errou! Tente novamente.")
                tentativas = tentativas+1
        print("######################")
        placar.append([nome, tentativas])

    print("Nome,Tentativas")

    for i in range(numero_de_jogadores):
        print(placar[i][0] + "," + str(placar[i][1]) )


# Função para implementar mensagem de que o jogo ainda não foi implementado
def ainda_nao_foi_implementado(nome):
    print(nome + " ainda não foi implementado.")





# O programa
# *******************************************************

# Menu
print("[1] Adivinha numero")
print("[2] Xadrez")
print("[3] Forca")
print("[4] Dungeons and Dragons")
# ****

print("Qual jogo quer jogar? ")
jogo = int(input())

if jogo == 1:
    # Adivinha numero
    jogo_de_adivinhar_numero()
elif jogo == 2:
    # Xadrez
    x = ainda_nao_foi_implementado("Xadrez")
    print(x)
    pass
elif jogo == 3:
    # Forca
    ainda_nao_foi_implementado("Forca")
    pass
elif jogo == 4:
    # Dungeons and Dragons
    ainda_nao_foi_implementado("Dungeons and Dragons")
    pass
else:
    print("Opção inválida") 
# *******************************************************













