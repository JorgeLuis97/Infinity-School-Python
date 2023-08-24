lista = [10, 16, 18, 19, 17, 15, 12, 20, 22]
par = []
impar = []
for i in range(len(lista)):
    if lista[i] % 2 == 0:
        par.append(lista[i])
    else:
        impar.append(lista[i])

print(f"Pares: {len(par)}")
print(f"Números pares: {par}\n")
print(f"Impares: {len(impar)}")
print(f"Números impares: {impar}")
