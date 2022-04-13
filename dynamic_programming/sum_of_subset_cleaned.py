def isSumSubset(arr, arrLen, requiredSum):
    
    
    
    subset = [[False for i in range(requiredSum + 1)] for i in range(arrLen + 1)]

    
    
    for i in range(arrLen + 1):
        subset[i][0] = True

    
    for i in range(1, requiredSum + 1):
        subset[0][i] = False

    for i in range(1, arrLen + 1):
        for j in range(1, requiredSum + 1):
            if arr[i - 1] > j:
                subset[i][j] = subset[i - 1][j]
            if arr[i - 1] <= j:
                subset[i][j] = subset[i - 1][j] or subset[i - 1][j - arr[i - 1]]

    
    
    
    print(subset[arrLen][requiredSum])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
