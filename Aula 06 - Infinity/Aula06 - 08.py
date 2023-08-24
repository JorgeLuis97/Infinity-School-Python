PAR = []
IMPAR = []

for i in range(1, 11):
    n = int(input("Digite um número: "))
    if n % 2 == 0:
        PAR.append(n)
    else:
       IMPAR.append(n)

print(f"QTD. Pares: {len(PAR)}")
print(f"Números pares: {PAR}\n")
print(f"QTD. impares: {IMPAR}")
print(f"Números impares: {IMPAR}")
