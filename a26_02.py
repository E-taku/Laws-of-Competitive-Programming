def isPrime(x: int) -> bool:
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

Q = int(input())
for i in range(Q):
    x = int(input())
    print("Yes" if isPrime(x) else "No")