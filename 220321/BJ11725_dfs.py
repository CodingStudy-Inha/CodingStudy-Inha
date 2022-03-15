# DFS 재귀 이용 풀이

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n=int(input())
tree=[[] for _ in range(n+1)]   # 트리 이중 list
ans=[0]*(n+1)   # 부모 노드 저장 list

for _ in range(n-1):
    a,b=map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)   # 트리 형태에 입력(append)

def dfs(n):
    for i in tree[n]:
        if ans[i]==0:   # 부모 노드가 없으면
            ans[i]=n    # 부모를 n으로 설정해주고
            dfs(i)      # dfs 재귀 실행

dfs(1)
for i in range(2,n+1):
    print(ans[i])