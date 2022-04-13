


def count_inversions_bf(arr):
    

    num_inversions = 0
    n = len(arr)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                num_inversions += 1

    return num_inversions


def count_inversions_recursive(arr):
    
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    P = arr[0:mid]
    Q = arr[mid:]

    A, inversion_p = count_inversions_recursive(P)
    B, inversions_q = count_inversions_recursive(Q)
    C, cross_inversions = _count_cross_inversions(A, B)

    num_inversions = inversion_p + inversions_q + cross_inversions
    return C, num_inversions


def _count_cross_inversions(P, Q):
    

    R = []
    i = j = num_inversion = 0
    while i < len(P) and j < len(Q):
        if P[i] > Q[j]:
            
            
            
            num_inversion += len(P) - i
            R.append(Q[j])
            j += 1
        else:
            R.append(P[i])
            i += 1

    if i < len(P):
        R.extend(P[i:])
    else:
        R.extend(Q[j:])

    return R, num_inversion


def main():
    arr_1 = [10, 2, 1, 5, 5, 2, 11]

    
    

    num_inversions_bf = count_inversions_bf(arr_1)
    _, num_inversions_recursive = count_inversions_recursive(arr_1)

    assert num_inversions_bf == num_inversions_recursive == 8

    print("number of inversions = ", num_inversions_bf)

    

    arr_1.sort()
    num_inversions_bf = count_inversions_bf(arr_1)
    _, num_inversions_recursive = count_inversions_recursive(arr_1)

    assert num_inversions_bf == num_inversions_recursive == 0
    print("number of inversions = ", num_inversions_bf)

    
    arr_1 = []
    num_inversions_bf = count_inversions_bf(arr_1)
    _, num_inversions_recursive = count_inversions_recursive(arr_1)

    assert num_inversions_bf == num_inversions_recursive == 0
    print("number of inversions = ", num_inversions_bf)


if __name__ == "__main__":
    main()
