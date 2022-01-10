n = int(input("Digite um número inteiro: "))
if n == 2 or (n != 1 and n % 2 == 1): # 2 é primo, 1 não é primo
    é_primo = True
else:
    é_primo = False  # pares maiores que 2 não são primos

# procure por um divisor ímpar de n entre 2 e n-1
divisor = 3
while divisor < n // 2 and é_primo:
    if n % divisor == 0:
        é_primo = False
    divisor += 2 


if é_primo: 
    print("primo");
else:
    print("não primo");