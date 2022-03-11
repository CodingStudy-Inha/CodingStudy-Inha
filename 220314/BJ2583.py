m,n,k=map(int,input().split())
s=[[0]*n for _ in range(m)]     # s list 0으로 초기화

dx=[0,0,-1,1]
dy=[-1,1,0,0]
cnt_lst=[]

for i in range(k):
    x1,y1,x2,y2=map(int,input().split())
    for j in range(y1,y2):
        for l in range(x1,x2):
            s[j][l]=1           # 입력받은 직사각형들을 s list에서 1로 처리해서 초기값(0)과 구분

for i in range(m):
    for j in range(n):
        if s[i][j]==0:          # s list가 0인 경우 = 직사각형이 아닌 영역 = 분리된 영역
            cnt=1
            s[i][j]=1
            q=[[i,j]]
                                # BFS를 이용해 해당 영역을 1로 채워주고 한칸 채울때마다 cnt++
            while q:            # 하나의 분리된 영역을 1로 다 채우면 ++한 cnt값을 cnt list에 저장
                x,y=q[0][0],q[0][1]
                del q[0]

                for l in range(4):
                    nx=x+dx[l]
                    ny=y+dy[l]
                    if 0<=nx<m and 0<=ny<n and s[nx][ny]==0:
                        s[nx][ny]=1
                        cnt+=1
                        q.append([nx,ny])
            cnt_lst.append(cnt)

cnt_lst.sort()
print(len(cnt_lst))             # cnt list의 원소 개수가 분리된 영역의 개수이고,
print(*cnt_lst)                 # 각 cnt값이 분리된 영역 각각의 크기이므로 정렬 후 출력