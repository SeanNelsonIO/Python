

from math import sqrt


def isPrime(number):
    

    
    assert isinstance(number, int) and (
        number >= 0
    ), "'number' must been an int and positive"

    status = True

    
    if number <= 1:
        status = False

    for divisor in range(2, int(round(sqrt(number))) + 1):

        
        
        if number % divisor == 0:
            status = False
            break

    
    assert isinstance(status, bool), "'status' must been from type bool"

    return status





def sieveEr(N):
    

    
    assert isinstance(N, int) and (N > 2), "'N' must been an int and > 2"

    
    beginList = [x for x in range(2, N + 1)]

    ans = []  

    
    for i in range(len(beginList)):

        for j in range(i + 1, len(beginList)):

            if (beginList[i] != 0) and (beginList[j] % beginList[i] == 0):
                beginList[j] = 0

    
    ans = [x for x in beginList if x != 0]

    
    assert isinstance(ans, list), "'ans' must been from type list"

    return ans





def getPrimeNumbers(N):
    

    
    assert isinstance(N, int) and (N > 2), "'N' must been an int and > 2"

    ans = []

    
    
    for number in range(2, N + 1):

        if isPrime(number):

            ans.append(number)

    
    assert isinstance(ans, list), "'ans' must been from type list"

    return ans





def primeFactorization(number):
    

    
    assert isinstance(number, int) and number >= 0, "'number' must been an int and >= 0"

    ans = []  

    

    factor = 2

    quotient = number

    if number == 0 or number == 1:

        ans.append(number)

    
    elif not isPrime(number):

        while quotient != 1:

            if isPrime(factor) and (quotient % factor == 0):
                ans.append(factor)
                quotient /= factor
            else:
                factor += 1

    else:
        ans.append(number)

    
    assert isinstance(ans, list), "'ans' must been from type list"

    return ans





def greatestPrimeFactor(number):
    

    
    assert isinstance(number, int) and (
        number >= 0
    ), "'number' bust been an int and >= 0"

    ans = 0

    
    primeFactors = primeFactorization(number)

    ans = max(primeFactors)

    
    assert isinstance(ans, int), "'ans' must been from type int"

    return ans





def smallestPrimeFactor(number):
    

    
    assert isinstance(number, int) and (
        number >= 0
    ), "'number' bust been an int and >= 0"

    ans = 0

    
    primeFactors = primeFactorization(number)

    ans = min(primeFactors)

    
    assert isinstance(ans, int), "'ans' must been from type int"

    return ans





def isEven(number):
    

    
    assert isinstance(number, int), "'number' must been an int"
    assert isinstance(number % 2 == 0, bool), "compare bust been from type bool"

    return number % 2 == 0





def isOdd(number):
    

    
    assert isinstance(number, int), "'number' must been an int"
    assert isinstance(number % 2 != 0, bool), "compare bust been from type bool"

    return number % 2 != 0





def goldbach(number):
    

    
    assert (
        isinstance(number, int) and (number > 2) and isEven(number)
    ), "'number' must been an int, even and > 2"

    ans = []  

    
    primeNumbers = getPrimeNumbers(number)
    lenPN = len(primeNumbers)

    
    i = 0
    j = None

    
    loop = True

    while i < lenPN and loop:

        j = i + 1

        while j < lenPN and loop:

            if primeNumbers[i] + primeNumbers[j] == number:
                loop = False
                ans.append(primeNumbers[i])
                ans.append(primeNumbers[j])

            j += 1

        i += 1

    
    assert (
        isinstance(ans, list)
        and (len(ans) == 2)
        and (ans[0] + ans[1] == number)
        and isPrime(ans[0])
        and isPrime(ans[1])
    ), "'ans' must contains two primes. And sum of elements must been eq 'number'"

    return ans





def gcd(number1, number2):
    

    
    assert (
        isinstance(number1, int)
        and isinstance(number2, int)
        and (number1 >= 0)
        and (number2 >= 0)
    ), "'number1' and 'number2' must been positive integer."

    rest = 0

    while number2 != 0:

        rest = number1 % number2
        number1 = number2
        number2 = rest

    
    assert isinstance(number1, int) and (
        number1 >= 0
    ), "'number' must been from type int and positive"

    return number1





def kgV(number1, number2):
    

    
    assert (
        isinstance(number1, int)
        and isinstance(number2, int)
        and (number1 >= 1)
        and (number2 >= 1)
    ), "'number1' and 'number2' must been positive integer."

    ans = 1  

    
    if number1 > 1 and number2 > 1:

        
        primeFac1 = primeFactorization(number1)
        primeFac2 = primeFactorization(number2)

    elif number1 == 1 or number2 == 1:

        primeFac1 = []
        primeFac2 = []
        ans = max(number1, number2)

    count1 = 0
    count2 = 0

    done = []  

    
    for n in primeFac1:

        if n not in done:

            if n in primeFac2:

                count1 = primeFac1.count(n)
                count2 = primeFac2.count(n)

                for i in range(max(count1, count2)):
                    ans *= n

            else:

                count1 = primeFac1.count(n)

                for i in range(count1):
                    ans *= n

            done.append(n)

    
    for n in primeFac2:

        if n not in done:

            count2 = primeFac2.count(n)

            for i in range(count2):
                ans *= n

            done.append(n)

    
    assert isinstance(ans, int) and (
        ans >= 0
    ), "'ans' must been from type int and positive"

    return ans





def getPrime(n):
    

    
    assert isinstance(n, int) and (n >= 0), "'number' must been a positive int"

    index = 0
    ans = 2  

    while index < n:

        index += 1

        ans += 1  

        
        
        while not isPrime(ans):
            ans += 1

    
    assert isinstance(ans, int) and isPrime(
        ans
    ), "'ans' must been a prime number and from type int"

    return ans





def getPrimesBetween(pNumber1, pNumber2):
    

    
    assert (
        isPrime(pNumber1) and isPrime(pNumber2) and (pNumber1 < pNumber2)
    ), "The arguments must been prime numbers and 'pNumber1' < 'pNumber2'"

    number = pNumber1 + 1  

    ans = []  

    
    
    while not isPrime(number):
        number += 1

    while number < pNumber2:

        ans.append(number)

        number += 1

        
        while not isPrime(number):
            number += 1

    
    assert (
        isinstance(ans, list) and ans[0] != pNumber1 and ans[len(ans) - 1] != pNumber2
    ), "'ans' must been a list without the arguments"

    
    return ans





def getDivisors(n):
    

    
    assert isinstance(n, int) and (n >= 1), "'n' must been int and >= 1"

    ans = []  

    for divisor in range(1, n + 1):

        if n % divisor == 0:
            ans.append(divisor)

    
    assert ans[0] == 1 and ans[len(ans) - 1] == n, "Error in function getDivisiors(...)"

    return ans





def isPerfectNumber(number):
    

    
    assert isinstance(number, int) and (
        number > 1
    ), "'number' must been an int and >= 1"

    divisors = getDivisors(number)

    
    assert (
        isinstance(divisors, list)
        and (divisors[0] == 1)
        and (divisors[len(divisors) - 1] == number)
    ), "Error in help-function getDivisiors(...)"

    
    return sum(divisors[:-1]) == number





def simplifyFraction(numerator, denominator):
    

    
    assert (
        isinstance(numerator, int)
        and isinstance(denominator, int)
        and (denominator != 0)
    ), "The arguments must been from type int and 'denominator' != 0"

    
    gcdOfFraction = gcd(abs(numerator), abs(denominator))

    
    assert (
        isinstance(gcdOfFraction, int)
        and (numerator % gcdOfFraction == 0)
        and (denominator % gcdOfFraction == 0)
    ), "Error in function gcd(...,...)"

    return (numerator // gcdOfFraction, denominator // gcdOfFraction)





def factorial(n):
    

    
    assert isinstance(n, int) and (n >= 0), "'n' must been a int and >= 0"

    ans = 1  

    for factor in range(1, n + 1):
        ans *= factor

    return ans





def fib(n):
    

    
    assert isinstance(n, int) and (n >= 0), "'n' must been an int and >= 0"

    tmp = 0
    fib1 = 1
    ans = 1  

    for i in range(n - 1):

        tmp = ans
        ans += fib1
        fib1 = tmp

    return ans
