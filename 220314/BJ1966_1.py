t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    lst=list(map(int,input().split()))  # 중요도 저장 list

    tmp=[0 for _ in range(n)]   # 위치 저장 list
    tmp[m]=1
    cnt=0

    while True:
        if lst[0]==max(lst):
            cnt+=1
            if tmp[0]==1:
                print(cnt)
                break
            else:
                del lst[0]
                del tmp[0]
        else:
            lst.append(lst[0])
            del lst[0]
            tmp.append(tmp[0])
            del tmp[0]

# lst 리스트에 프린트의 중요도를 입력 및 저장하고, tmp 리스트에 프린트의 위치를 저장한다
# tmp[]는 전부 0으로 초기화하고, 그 중 m번째 프린트의 위치를 기억하기 위해 tmp[m]만 1로 선언해둔다.
# 맨앞이 최대 중요도 프린트이면 cnt++를 한 뒤, 위치가 1(=m번째 프린트를 의미) 이면 누적 cnt를 출력하고 종료
# 맨앞이 m번째 프린트가 아니면 그대로 프린트를 하고 중요도 및 위치 리스트 맨앞 삭제
# 맨앞이 최대 중요도 프린트가 아니면 중요도 및 위치 리스트의 맨앞으로 맨뒤로 append하고 맨앞 삭제