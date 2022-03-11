t=int(input())

dp=[1,2,4]
for i in range(3,10):
    tmp=dp[i-3]+dp[i-2]+dp[i-1]
    dp.append(tmp)

for _ in range(t):
    n=int(input())
    print(dp[n-1])

# dp문제
# 1,2,3까지는 합으로 나타내는 방법을 직접 구한다 (1,2,4)
# 그 이후는 점화식으로 dp 리스트에 저장하고 입력값 n에 따라 dp를 출력한다.