a = int(input("informe o lado A: "))
b = int(input("informe o lado B: "))
c = int(input("informe o lado C: "))

if a == b and a == c:
    print("É equilatero")
elif a == b and a != c or b == c and b != a or c == a and c != b:
    print("É Isoceles")
elif a != b and a != c:
    print("É Escaleno")
