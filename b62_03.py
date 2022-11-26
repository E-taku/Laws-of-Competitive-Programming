# import sys
# from collections import defaultdict
# sys.setrecursionlimit(10 ** 9)

# N,M = map(int,input().split())

# G = defaultdict(list)

# for i in range(M):
#     a,b = map(int,input().split())
#     G[a].append(b)
#     G[b].append(a)

# visited = [False] * (N+1)
# path = []
# def dfs( i: int,):
#     path.append(i)
#     if i == N:
#         print(*path)
#         exit()
#     visited[i] = True
#     for next in G[i]:
#         if visited[next] == False:
#             dfs(next)
#     path.pop()

# dfs(1)





import sys
from collections import defaultdict
sys.setrecursionlimit(10 ** 9)

class Single_path():
    """
    頂点数 N、辺数 M の連結なグラフが与えられる。 このグラフについて、頂点 1 から頂点 N までの単純パスを一つ出力。

    """
    def __init__(self):
        self.path = []

    def input(self):
        self.N,self.M = map(int,input().split())

        self.G = defaultdict(list)

        for i in range(self.M):
            a,b = map(int,input().split())
            self.G[a].append(b)
            self.G[b].append(a)



    def simple_path(self):
        visited = [False] * (self.N+1)
        def dfs(self,i: int):
            self.path.append(i)
            if i == self.N:
                print(*self.path)
                exit()
                return self.path
            visited[i] = True
            for next in self.G[i]:
                if visited[next] == False:
                    dfs(self,next)
            self.path.pop()
        dfs(self,1)

sp = Single_path()
sp.input()
sp.simple_path()
