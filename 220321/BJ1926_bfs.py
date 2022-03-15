# bfs deque 이용 풀이
import sys
input=sys.stdin.readline
from collections import deque

def bfs(x,y):
    cnt=1
    q=deque()
    q.append((x,y))
    visited[x][y]=True

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]==1 and visited[nx][ny]==False:
                visited[nx][ny]=True
                q.append((nx,ny))
                cnt+=1
    return cnt

n,m=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]

visited=[[0]*m for _ in range(n)]

dx=[0,0,1,-1]
dy=[1,-1,0,0]

num,max_cnt=0,0
for i in range(n):
    for j in range(m):
        if graph[i][j]==1 and visited[i][j]==False:
            max_cnt=max(max_cnt, bfs(i,j))
            num+=1

print(num)
print(max_cnt)