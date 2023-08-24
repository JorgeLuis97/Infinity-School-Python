x = int(input("Digite valor de X: "))
y = int(input("Digite valor de Y: "))

if x > 0 and y > 0:
    print("Está no primeiro quadrante")
elif x < 0 < y:
    print("Está no segundo quadrante")
elif x < 0 and y < 0:
    print("Está no terceiro quadrante")
elif y < 0 < x:
    print("Está no Quarto quadrante")
else:
    print("Está no meio")
