#Nesse jogo, n peças são inicialmente dispostas numa mesa ou tabuleiro.
#Dois jogadores jogam  alternadamente, retirando pelo menos 1 e no
#máximo m peças cada um.
#Quem tirar as últimas peças possíveis ganha o jogo.

#Existe uma estratégia para ganhar o jogo que é muito simples:
#ela consiste em deixar sempre múltiplos de (m+1) peças ao jogador oponente.

def computador_escolhe_jogada(n, m):
    '''
    Devolve o número de peças removidas pela jogada.
    '''


def usuario_escolhe_jogada(n, m):
    '''
    Devolve o número de peças removidas pela jogada.
    '''


def partida():
    print("Você escolheu partida!")


def campeonato():
    '''
    Chama a função partida() 3 vezes.
    '''
    print("Você escolheu campeonato!")


def main():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - para jogar uma partida isolada")
    escolha = int(input("2 - para jogar um campeonato "))
    if escolha == 1:
        partida()
    else:
        if escolha == 2:
            campeonato()

main()
