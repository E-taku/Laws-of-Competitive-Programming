N = int(input())
A = list(map(int,input().split()))


for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(i+2,N):
            if (A[i] + A[j] + A[k]) == 1000:
                print("Yes")
                exit()
print("No")