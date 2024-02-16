if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    lista = []

    for a in range(x + 1):
        for b in range(y + 1):
            for c in range(z + 1):
                if a + b + c != n:
                    lista_temporaria = [a, b, c]
                    lista.append(lista_temporaria)

    print(lista)







