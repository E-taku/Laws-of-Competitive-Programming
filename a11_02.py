class BinarySearch_1:
    def __init__(self,x: int,A: list):
        self.x = x # 探したい値
        self.A = sorted(A) # 配列
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
                return M + 1
            if self.x > self.A[M]:
                L = M + 1
        return -1


N,X = map(int,input().split())
A = list(map(int,input().split()))
bs = BinarySearch_1(X,A)
print(bs.idx)