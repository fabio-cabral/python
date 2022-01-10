numero = input("Digite um número inteiro: ")
tamanho = len(numero)
numero = int(numero)
aux = 0
valor = 0
while tamanho >= 0:
    aux = numero % 10
    numero = numero // 10
    valor = aux + valor
    tamanho = tamanho - 1
print(valor)
