Q = int(input())

def isPrime(x):
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

for i in range(Q):
    x = int(input())
    print('Yes' if isPrime(x) else 'No')