# BFS deque 이용 풀이

import sys
input = sys.stdin.readline
from collections import deque

n=int(input())
graph=[[] for _ in range(n+1)]
ans=[0]*(n+1)

for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(node):
    q=deque()
    q.append(1)
    while q:
        node=q.popleft()
        for i in graph[node]:
            if ans[i]==0:
                ans[i]=node
                q.append(i)

bfs(1)
for i in range(2,n+1):
    print(ans[i])