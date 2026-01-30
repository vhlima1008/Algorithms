def linear_search(array, value):
    stringfy = ''
    count = 1
    size = len(array) - 1
    for i in range(0, size):
        if value == array[i]:
            stringfy += f"Step {count}: current value is {array[i]}, it is equal {value}." + '\n'
            return stringfy
        stringfy += f"Step {count}: current value is {array[i]}, it isn't equal {value}." + '\n'
        count += 1
    return -1

array = [1,2,3,4,5,6,7,8,9,10]
value = 6

print(linear_search(array, value))
