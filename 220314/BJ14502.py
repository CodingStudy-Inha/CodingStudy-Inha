graph=[]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
ans=0

def bfs():
    global ans
    graph2=[[0]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            graph2[i][j]=graph[i][j]

    cnt=0
    tmp=[]
    for i in range(n):
        for j in range(m):
            if graph2[i][j]==2:
                tmp.append([i,j])
    
    while tmp:
        x,y=tmp[0][0],tmp[0][1]
        del tmp[0]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<n and 0<=ny<m:
                if graph2[nx][ny]==0:
                    graph2[nx][ny]=2
                    tmp.append([nx,ny])
    
    for s in graph2:
        for k in s:
            if k==0:
                cnt+=1
    ans=max(ans,cnt)

def new_wall(t):
    if t==3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j]==0:
                graph[i][j]=1
                new_wall(t+1)
                graph[i][j]=0

n,m=map(int,input().split())
for _ in range(n):
    graph.append(list(map(int,input().split())))

new_wall(0)
print(ans)


# https://pacific-ocean.tistory.com/262
# https://hongcoding.tistory.com/m/130
# BFS이용, 두개 블로그 적절히 참고하여 queue(list)로 bfs돌리는 풀이
# 아직까진 dfs,bfs 완벽하게 익히지는 못했지만 공통적인 코드 틀은 익숙해진 정도