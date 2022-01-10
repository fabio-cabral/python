n = int(input("Digite o valor de n: "))
fatorial = 1
contador = 1
while contador <= n:
    fatorial = fatorial * contador
    contador = contador + 1
print(fatorial)