#Nesse jogo, n peças são inicialmente dispostas numa mesa ou tabuleiro.
#Dois jogadores jogam  alternadamente, retirando pelo menos 1 e no
#máximo m peças cada um.
#Quem tirar as últimas peças possíveis ganha o jogo.

#Existe uma estratégia para ganhar o jogo que é muito simples:
#ela consiste em deixar sempre múltiplos de (m+1) peças ao jogador oponente.

def computador_escolhe_jogada(n, m):
    '''
    Devolve o número de peças removidas pela jogada do computador.
    '''
    peçasRemovidasComputador = 1

    while peçasRemovidasComputador != m:        
        if (n - peçasRemovidasComputador) % (m + 1) == 0:
            return peçasRemovidasComputador
        else:
            peçasRemovidasComputador += 1

    return peçasRemovidasComputador
    


def usuario_escolhe_jogada(n, m):
    '''
    Devolve o número de peças removidas pela jogada do usuário.
    '''
    jogadaValida = False

    while not jogadaValida:
        peçasRemovidasUsuario = int(input("Quantas peças você vai tirar? "))
        if peçasRemovidasUsuario > m or peçasRemovidasUsuario < 1:
            print()
            print("Oops! Jogada inválida! Tente de novo.")
            print()
        else:
            jogadaValida = True

    return peçasRemovidasUsuario
    


def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    if n % (m + 1) == 0: 
        computadorComeça = False
        print()
        print("Você começa!")
    else:
        computadorComeça = True
        print()
        print("Computador começa!")
    while n > 0:
        if computadorComeça:
            peçasComputador = computador_escolhe_jogada(n, m)
            n = n - peçasComputador
            if peçasComputador == 1:
                print()
                print("O computador tirou uma peça.")
            else:
                print()
                print("O computador tirou", peçasComputador, "peças.")

            computadorComeça = False
        else:
            peçasUsuario = usuario_escolhe_jogada(n, m)
            n = n - peçasUsuario
            if peçasUsuario == 1:
                print()
                print("Você tirou uma peça.")
            else:
                print()
                print("Você tirou", peçasUsuario, "peças.")
            computadorComeça = True
        if n == 1:
            print("Agora resta apenas uma peça no tabuleiro.")
            print()
        else:
            if n != 0:
                print("Agora restam,", n, "peças no tabuleiro.")
                print()

    print("Fim do jogo! O computador ganhou!")


def campeonato():
    '''
    Chama a função partida() 3 vezes.
    '''
    print()
    print("Você escolheu um campeonato!")
    rodada = 1
    while rodada <= 3:
        print()
        print("**** Rodada ", rodada, " ****")
        print()
        partida()
        rodada = rodada + 1
    print()
    print("**** Final do campeonato! ****")
    print()
    print("Placar: Você 0 X 3 Computador")


def main():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print()
    print("1 - para jogar uma partida isolada")
    escolha = int(input("2 - para jogar um campeonato "))
    if escolha == 1:
        print()
        print("Você escolheu partida!")
        partida()
    else:
        if escolha == 2:
            print()
            campeonato()

main()
