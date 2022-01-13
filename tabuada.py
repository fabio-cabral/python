##linha = 1
##coluna = 1
##while linha <= 10:
##    while coluna <= 10:
##        print(linha * coluna, end = "\t")
##        coluna +=1
##    linha +=1
##    print()
##    coluna = 1

    
print("a")
tab = 1
while tab <= 10:
    print("Tabuada do", tab, ":", end="\t")
    i = 1
    while i <= 10:
        print(tab*i, end = "\t")
        i = i + 1
    print()
    tab = tab + 1


print()
print("B")
tab = 1
while tab <= 10:
    i = 1
    while i <= 10:
        print(tab,"x",i,"=",tab*i)
        i = i + 1
    print()
    tab = tab + 1


print()
print("C")
tab = 0
while tab < 10:
    tab = tab + 1
    i = 0
    while i < 10:
        i = i + 1
        print(tab,"x",i,"=",tab*i)
    print()


print()
print("D")
tab = 1
i = 1
while tab <= 10 and i <= 10:
    print(tab,"x",i,"=",tab*i)
    i = i + 1
    tab = tab + 1
print()

print()
print("E")
tab = 1
while tab <= 10:
    print("Tabuada do", tab, ":", end="\t")
    i = 1
    print(tab*i, end = "\t")
    i = i + 1
    print()
    tab = tab + 1
