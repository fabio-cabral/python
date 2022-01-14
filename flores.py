flores = ["margarida", "rosa", "tulipa", "cravo"]
tam = len(flores) - 1
while tam >= 0:
    print(flores[tam], end=", ")
    tam = tam - 1

print()
animais = ["gato", "cachorro", "papagaio", "arara", "jacaré"]
for x in range(len(animais)):
    print("--> ", animais[x])

valores = []
for i in range(1, 10):
    if i % 2 == 0:
        valores.append(i)
