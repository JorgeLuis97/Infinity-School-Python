lista = [10, 16, 18, 19, 17, 15, 12, 20, 22]
maior = lista[0]
menor = lista[0]
for i in range(len(lista)):
    if lista[i] > maior:
        maior = lista[i]
    if lista[i] < menor:
        menor = lista[i]

print(f"Maior: {maior}")
print(f"Menor: {menor}")
