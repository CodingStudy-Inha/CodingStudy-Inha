n=input().split()

for _ in range(len(n)):
    for i in range(1,len(n)):
        if n[i]<n[i-1]:
            n[i],n[i-1]=n[i-1],n[i]
            print(*n)

# 1번 풀이를 이중for문으로 간략화한 풀이
# 버블 정렬