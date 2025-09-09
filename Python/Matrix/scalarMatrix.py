def scalarMat(n, K):
    nul = K - K
    return [[K if x == y else nul for x in range(n)] for y in range(n)]

while True:
    try:    
        n = int(input('Write the rows/colunms number: '))
        K = float(input('Write the diagonal number: '))
        if K == 1: typ = 'Identity'; 
        else: typ = 'Scalar'; 

        mat = scalarMat(n,K)
        print('')
        print(f'It is a {typ} Matrix:','\n')
        for row in mat:
            print(row)
        print('')
    except ValueError:
        print('\n-> Wrong value.\n')