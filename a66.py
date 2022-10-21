# Union-Find 木
class unionfind:
    # n 頂点のUnion-Find 木を作成
    # (ここでは頂点番号が 1-indexed になるように実装しているが、0-indexed の場合は par,size のサイズはnでよい)
    def __init__(self,n):
        self.n = n
        self.par = [-1] * (n+1) # 最初は親が無い
        self.size = [1] * (n+1) # 最初はグループの頂点数が1

    # 頂点 x の根を返す関数
    def root(self,x):
        # 1個先（親）がなくなる（つまり根に到達する）まで、１個先（親）に進み続ける
        while self.par[x] != -1:
            x = self.par[x]
        return x

    # 要素 u,v を結合する関数
    def unite(self,u,v):
        rootu = self.root(u) # 頂点uの根を取得
        rootv = self.root(v) # 頂点vの根を取得

        if rootu != rootv:
            # u と v が異なるグループの時のみ処理を行う
            if self.size[rootu] < self.size[rootv]:
                self.par[rootu] = rootv
                self.size[rootv] += self.size[rootu]
            else:
                self.par[rootv] = rootu
                self.size[rootu] += self.size[rootv]

    #  要素 u と v が同一のグループかどうかを返す関数
    def same(self,u,v):
        return self.root(u) == self.root(v)

N,Q = map(int,input().split())

uf = unionfind(N)
for i in range(Q):
    q,u,v = map(int,input().split())
    if q == 1:
        uf.unite(u,v)
    elif q == 2:
        if uf.same(u,v):
            print('Yes')
        else:
            print("No")