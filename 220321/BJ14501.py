n=int(input())
time,cost=[],[]
dp=[]

for _ in range(n):
    a,b=map(int,input().split())
    time.append(a)
    cost.append(b)
    dp.append(b)
dp.append(0)    # 퇴사 전날(마지막날)의 dp[] 값을 구하기 위해 dp 마지막에 0을 추가한다.

for i in reversed(range(n)):    # dp[] 뒤쪽부터(퇴사일에 가까운날부터) check 
    if time[i]+i<=n:            # 상담시간(time[]) + 상담날짜(index) 가 퇴사일보다 작으면,
        dp[i] = max(dp[i+1], dp[time[i]+i] + cost[i])   # 이 부분 생각해내는게 어려운듯
        # (역순이므로) 이전까지의 dp[](=최대상담비)를 유지하는 것과 해당 index(날짜)에 상담을 하는 경우 중 max값을 현재 dp에 저장
    else:
        dp[i]=dp[i+1]           # 상담기간이 퇴사일을 넘어가면, 단순히 이전의 dp[](=최대상담비)를 그대로 저장
print(dp[0])                    # 역순으로 dp를 구했으므로 최종 dp[0]를 출력하면 최대 상담비.