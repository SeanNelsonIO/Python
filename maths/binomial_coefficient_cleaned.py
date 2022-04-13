def binomial_coefficient(n, r):
    
    C = [0 for i in range(r + 1)]
    
    C[0] = 1
    for i in range(1, n + 1):
        
        j = min(i, r)
        while j > 0:
            C[j] += C[j - 1]
            j -= 1
    return C[r]


print(binomial_coefficient(n=10, r=5))
