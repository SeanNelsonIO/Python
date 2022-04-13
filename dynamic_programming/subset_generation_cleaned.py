


def combination_util(arr, n, r, index, data, i):
    
    if index == r:
        for j in range(r):
            print(data[j], end=" ")
        print(" ")
        return
    
    if i >= n:
        return
    
    data[index] = arr[i]
    combination_util(arr, n, r, index + 1, data, i + 1)
    
    
    
    combination_util(arr, n, r, index, data, i + 1)
    
    
    


def print_combination(arr, n, r):
    
    data = [0] * r
    
    combination_util(arr, n, r, 0, data, 0)



arr = [10, 20, 30, 40, 50]
print_combination(arr, len(arr), 3)

