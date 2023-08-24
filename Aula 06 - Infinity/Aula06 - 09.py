Lista = []

for i in range(1, 6):
    n = input("Digite um item: ").upper()
    Lista.append(n)

print(f"Lista: {Lista}\n")

pergunta = input("Qual item deseja remover? ").upper()

if pergunta in Lista:
    Lista.remove(pergunta)
else:
    print("Item não está na lista\n")

print(f"Lista: {Lista}")
