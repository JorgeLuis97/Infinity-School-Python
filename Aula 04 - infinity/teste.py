def teste_perfeito(num):
    cont = 0
    for i in range(1, num):
        if num % i == 0:
            cont += i

    if cont == num:
        return True
    else:
        return False


print('--- Teste de número perfeito ---')
if teste_perfeito(int(input('Qual número deseja testar? '))):
    print('É perfeito')
else:
    print('Não é perfeito')
