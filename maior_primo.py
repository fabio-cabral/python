def éPrimo(n):
    if n == 2 or (n != 1 and n % 2 == 1): # 2 é primo, 1 não é primo
        é_primo = True
    else:
        é_primo = False # pares maiores que 2 não são primos

# procure por um divisor ímpar de n entre 2 e n-1
    divisor = 3
    while divisor < n // 2 and é_primo:
        if n % divisor == 0:
            é_primo = False
        divisor += 2
    return é_primo

def maior_primo(n):
    valor=1
    maior=0
    while valor <= n:
        if éPrimo(valor):
           maior=valor
        valor = valor + 1
    return maior
