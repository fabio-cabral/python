def fizzbuzz(numero):
        if (numero % 3 == 0) and not (numero % 5 == 0):
                return "Fizz"
        else:
                if not (numero % 3 == 0) and (numero % 5 == 0):
                        return "Buzz"
                else:
                        if (numero % 3 == 0) and (numero % 5 == 0): # Verifica se o número é divisível por 3 e por 5
                                return "FizzBuzz"
                        else:
                                return numero
