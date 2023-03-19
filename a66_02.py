# Union-Find木
class UnionFind:
    # n 頂点のUnion-Find木を作成
    # （ここでは頂点番号が1-indexed になるように実装しているが、0-indexdの場合はpar,size のサイズはnでよい）
    def __init__(self, n):
        self.n = n
        self.par = [-1] * (n+1) # 最初は親がない
        self.size = [1] * (n+1) # 最初はグループの頂点数が1
        
    # 頂点 x の値を返す関数
    def root(self, x):
        # 1個先（親）がなくなる（つまり根に到達する）まで、1個先（親）に進み続ける
        while self.par[x] != -1:
            x = self.par[x]
        return x
    
    # 要素 u, v を結合する関数
    def unite(self, u, v):
        rootu = self.root(u) # 頂点uの根を取得
        rootv = self.root(v) # 頂点vの根を取得
        
        if rootu != rootv:
            # uとvが異なるグループの時のみ処理を行う
            if self.size[rootu] < self.size[rootv]:
                self.par[rootu] = rootv
                self.size[rootv] += self.size[rootu]
            else:
                self.par[rootv] = rootu
                self.size[rootu] += self.size[rootv]
    
    # 要素u, v が合一のグループかどうかを返す関数
    def same(self, u, v):
        return self.root(u) == self.root(v)

N, Q = map(int,input().split())
uf = UnionFind(N)

for i in range(Q):
    q,u,v = map(int,input().split())
    if q == 1:
        uf.unite(u, v)
    elif q == 2:
        if uf.same(u,v):
            print('Yes')
        else:
            print("No")
    