Lista = ["mouse", "teclado", "fone", "gabinete", "monitor"]
maior = Lista[0]

for i in Lista:
    if len(i) > len(maior):
        maior = i

print(maior)
