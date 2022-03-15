import sys
input=sys.stdin.readline

dx=[-1,1,0,0]
dy=[0,0,-1,1]   # 순서대로 좌,우,하,상
L=[2,3,1,0]
R=[3,2,0,1]     # 각 방향에 따라 상이한 index 지정

t=int(input())
for _ in range(t):
    path=input()

    min_x,min_y,max_x,max_y=0,0,0,0
    x,y,d=0,0,0

    for k in path:
        if k=='L':      # 왼쪽 방향 전환 (d값을 인덱스로 하는 L[d]로 d값 변경)
            d=L[d]
            continue
        elif k=='R':    # 오른쪽 방향 전환 (d값을 인덱스로 하는 R[d]로 d값 변경)
            d=R[d]
            continue
        elif k=='F':    # 한칸 앞으로 이동 (x,y 둘다 증가)
            x=x+dx[d]
            y=y+dy[d]
        elif k=='B':    # 한칸 뒤로 이동 (x,y 둘다 감소)
            x=x-dx[d]
            y=y-dy[d]
    
        min_x=min(min_x, x)
        min_y=min(min_y, y)
        max_x=max(max_x, x)
        max_y=max(max_y, y)

    ans=abs(max_x-min_x)*abs(max_y-min_y)
    print(ans)