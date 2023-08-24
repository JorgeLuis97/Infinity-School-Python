count = 1
while count < 11:
    n = int(input(f"Digite o {count}º número: "))
    if n % 2 == 0:
        print(f"{n} é PAR")
    elif n % 2 != 0:
        print(f"{n} é impar")
    count += 1
