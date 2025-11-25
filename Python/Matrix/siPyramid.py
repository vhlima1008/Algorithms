def piramide(n):
    div = n // 2
    for linha in range(int((1+ n)/2)):
        for coluna in range (n):
            if coluna >=div - linha and coluna <=div + linha:
                print("1", end=" ")
            else:
                print(" ", end=" ")
        print()

piramide(7)

