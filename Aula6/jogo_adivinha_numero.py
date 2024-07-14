import random # Para usar o rand.randint()


# Quantos vão jogar?
numero_de_jogadores = int(input("Quantos jogadores? "))
# Lista para guardar as pontuações
placar = []


# Rodando o jogo uma vez para cada jogador
i = 0
while i < numero_de_jogadores:
    i = i + 1

    # Pega o nome do jogador
    nome = input("Qual seu nome? ")
    # Sorteia um número
    numero_secreto = random.randint(1,10)
    

    tentativas = 1
    acertou = False
    # Enquanto não acertar, continuamos perguntando
    while not acertou:
        palpite = int(input("Adivinhe um numero de 1 a 10: "))
        if palpite == numero_secreto:
            print("Acertou! Parabéns!")
            acertou = True
        else:
            print("Errou! Tente novamente.")
            tentativas = tentativas+1
    # Coloquei esse print para melhor visualizar o fim de uma partida e início da outra
    print("######################")
    # Coloca a pontuação do jogador na lista
    placar.append([nome, tentativas])
# *********************************************


# Imprimindo o placar
print("Nome,Tentativas")
for i in range(numero_de_jogadores):
    print(placar[i][0] + "," + str(placar[i][1]) )
# **********************************************
