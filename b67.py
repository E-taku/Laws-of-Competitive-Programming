# union-find木

class unionfind:
    def __init__(self,n):
        self.n = n
        self.par = [-1] * (n+1)
        self.size = [1] * (n+1)

    def root(self,x):
        while self.par[x] != -1:
            x = self.par[x]
        return x
    
    def unite(self,u,v):
        rootu = self.root(u)
        rootv = self.root(v)
        if rootu != rootv:
            if self.size[rootu] < self.size[rootv]:
                self.par[rootu] = rootv
                self.size[rootv] += self.size[rootu]
            else:
                self.par[rootv] = rootu
                self.size[rootu] += self.size[rootv]

    def same(self,u,v):
        return self.root(u) == self.root(v)

N,M = map(int,input().split())
edges = [ list(map(int, input().split())) for i in range(M) ]

# 辺を長さの小さい順にソートする
edges.sort(key=lambda x:x[2],reverse=True)

# 最小全域木を求める
uf = unionfind(N)
ans = 0
for a,b,c in edges:
    if not uf.same(a,b):
        uf.unite(a,b)
        ans += c

print(ans)