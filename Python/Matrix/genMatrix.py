while True:
    try:    
        mat = [];
        # n = int(input('Write the n number: '))
        row = 5
        col = 9
        mid = int(col-1)/2
        print(mid)

        # para funcionar o ultimo caso, tem que colocar col == n impar, row == col - 2

        for r in range(row):
            rowMat = []
            for c in range(col):
                # if c == (row - 1) - r:
                # if c == r:
                # if c == r or c == (row - 1 - r):
                # if c == mid:
                # if r == mid:
                # if r == mid or c == mid:
                # if c >= (row - 1) - r:
                # if c <= r + mid:
                if c >= (row - 1) - r and c <= r + mid:
                    v = 1
                else:
                    v = 0
                rowMat.append(v)
            mat.append(rowMat)

        print('')
        for row in mat:
            print(row)
        print('')

        break
    except ValueError:
        print('\n-> Wrong value.\n')