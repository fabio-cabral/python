meuCartao = int(input("Digite o número do seu cartão de crédito: "))
cartaoLido = 1
encontreiMeuCartaoNaLista = False
while cartaoLido != 0:
    cartaoLido = int(input("Digite o número do próximo cartão de crédito: "))
    if cartaoLido == meuCartao:
        encontreiMeuCartaoNaLista = True
        
if encontreiMeuCartaoNaLista:
    print("Ufa, meu cartão está na lista")
else:
    print("Xii, meu cartão não está na lista")