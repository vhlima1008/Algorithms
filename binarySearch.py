def binSearch(array, number):
    low = 0; high = len(array) - 1; i = 1 
    while (high >= low):
        mid = int(low) + int(round((high-low)/2,0))
        if (array[mid] == number):
            return f'is at index {mid}, interactions needed: {i}';
        elif (array[mid] > number):
            high = mid - 1
        else:
            low = mid + 1
        i += 1
    return 'not exists'

arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
n = int(input('Search for a number: '))

result = binSearch(arr,n)
print('The element',result)