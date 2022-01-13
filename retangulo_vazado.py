largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
largura_original = largura
altura_original = altura
while altura > 0:
    while largura > 0:
        if altura == 1 or altura == altura_original or largura == 1 or largura == largura_original:
            print("#", end = "")
        else:
            print(" ", end = "")
        largura = largura - 1
        if largura == 0:
            print()
    altura = altura -1
    largura = largura_original
