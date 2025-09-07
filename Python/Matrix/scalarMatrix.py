def scalarMat(n, K):
    nul = K - K
    return [[K if x == y else nul for x in range(n)] for y in range(n)]

n = 3
K = 2
if K == 1: typ = 'Identity'; 
else: typ = 'Scalar'; 

mat = scalarMat(n,K)

print(f'It is a {typ} Matrix:')
for row in mat:
    print(row)