n=int(input())
lst=[]
for _ in range(n):
    num=list(map(int,input().split()))
    lst.append(num)

k=2     # 맨윗줄 제외하고 두번째줄부터 k++ 해가며 한줄씩 진행
for i in range(1,n):
    for j in range(k):
        if j==0:    # 라인의 처음
            lst[i][j] += lst[i-1][j]
        elif i==j:  # 라인의 끝         # 이 둘은 바로 위에 수를 더해주면 됨
            lst[i][j] += lst[i-1][j-1]
        else:       # 나머지는 왼쪽위, 오른쪽위 수 중에 더 큰 값을 더해주면 됨
            lst[i][j] += max(lst[i-1][j],lst[i-1][j-1])
    k+=1

print(max(lst[n-1]))