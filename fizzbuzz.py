numero = int(input("Digite um número inteiro: "))
if (numero % 3 == 0) and (numero % 5 == 0): # Verifica se o número é divisível por 3 e por 5
	print("FizzBuzz")
else:
	print(numero)