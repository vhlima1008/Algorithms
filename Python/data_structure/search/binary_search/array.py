def binary_search(array, value):
    stringfy = ''
    count = 1
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if array[mid] == value:
            stringfy += f"Step {count}: mid is {array[mid]}, it's equal {value}." + '\n' 
            return stringfy
        elif array[mid] < value:
            low = mid + 1
            stringfy += f"Step {count}: mid is {array[mid]}, it's smaller than {value}." + '\n' 
        else:
            high = mid - 1
            stringfy += f"Step {count}: mid is {array[mid]}, it's bigger than {value}." + '\n' 
        count += 1
    return -1

array = [1,2,3,4,5,6,7,8,9,10]
value = 6

print(binary_search(array, value))
