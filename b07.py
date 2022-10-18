T = int(input())
N = int(input())

employee = [0] *(T+2)

for i in range(N):
    l,r = map(int,input().split())
    employee[l] += 1
    employee[r] -= 1

for i in range(T):
    employee[i+1] += employee[i]
    print(employee[i])

