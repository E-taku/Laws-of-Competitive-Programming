class BinarySearch_1:
    def __init__(self,x: int,A: list):
        self.x = x # 探したい値
        # self.A = sorted(A) # 配列
        self.A = A # 配列
        self.N = len(A)
        self.idx = self.search()

    def search(self):
        L = 0
        R = self.N - 1

        while L <= R:
            M = (L + R) // 2
            if self.x < self.A[M]:
                R = M - 1
            if self.x == self.A[M]:
                return M
            if self.x > self.A[M]:
                L = M + 1
        return L


N = int(input())
A = list(map(int,input().split()))
A = sorted(A)
Q = int(input())
for i in range(Q):
    x = int(input())
    bs = BinarySearch_1(x,A)
    print(bs.idx)