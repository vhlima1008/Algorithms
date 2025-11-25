n = int(input('Qual tamanho da piramide?'))

for i in range(1, n+1):
    espaco = '' * (n-1)
    asteriscos = '*' * (2 * i - 1)
    print(asteriscos + espaco)