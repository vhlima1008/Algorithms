arr1 = []; arr2 = []; vArr1 = 0; vArr2 = 0;

def genMat(c, r):
    return [[1 for x in range(c)] for y in range(r)]

while True:
    try:    
        col = int(input('Write the columns number: '))
        row = int(input('Write the rows number: '))

        mat = genMat(col, row)

        for x in range(0,row):
            for y in range(0,col):
                mat[x][y] = float(input('Write a value: '))
        
        if row == 1 and col == 1: type1 = ' Singleton'
        elif row == 1: type1 = ' Row';
        elif col == 1: type1 = ' Column';
        elif row < col: type1 = ' Horizontal';
        elif row > col: type1 = ' Vertical';
        else: type1 = ' Square'

        print('')
        print(f'It is a{type1} Matrix:','\n')
        for row in mat:
            print(row)
        print('')
    
    except ValueError:
        print('\n-> Wrong value.\n')