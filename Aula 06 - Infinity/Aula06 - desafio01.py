lista = [5, 7, 9, 3, 2, 10, 15, 16]
naoprimos = []
qtdprimos = []
for i in range(len(lista)):
    n = lista[i]
    eprimo = 0
    for j in range(1, n + 1):
        if n % j == 0:
            eprimo += 1
    if eprimo == 2:
        qtdprimos.append(lista[i])
    else:
        naoprimos.append(lista[i])

print(f"Qtd. de Primos: {len(qtdprimos)}")
print(f"Números Primos: {qtdprimos}\n")
print(f"Qtd. de não primos: {len(naoprimos)}")
print(f"Números não Primos: {naoprimos}")
