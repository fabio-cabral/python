largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
largura_original = largura
while altura > 0:
    while largura > 0:
        print("#", end = "")
        largura = largura - 1
        if largura == 0:
            print()
    altura = altura -1
    largura = largura_original
