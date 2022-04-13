


def solution(n: int = 100) -> int:
    
    collectPowers = set()

    currentPow = 0

    N = n + 1  

    for a in range(2, N):
        for b in range(2, N):
            currentPow = a**b  
            collectPowers.add(currentPow)  
    return len(collectPowers)


if __name__ == "__main__":
    print("Number of terms ", solution(int(str(input()).strip())))
