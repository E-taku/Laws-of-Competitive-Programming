N = int(input())

def f(x):
    return x * x * x + x
L = 1
R = 100
for i in range(20):
    M = (L+R) // 2
    val = f(M)

    if val > N:
        R = M
    else:
        L = M

print(M)