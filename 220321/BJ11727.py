# 풀이1. 배열(list) 이용 DP 점화식 적용
n=int(input())
dp=[0]*1001
dp[1]=1
dp[2]=3
for i in range(3,1001):
    dp[i]=dp[i-1]+dp[i-2]*2
print(dp[n]%10007)

# 풀이2. 같은 방법이지만 list에 append하는 방식으로 점화식 적용
n=int(input())
dp=[0,1,3]
for i in range(3,1001):
    dp.append(dp[i-1]+dp[i-2]*2)
print(dp[n]%10007)

# 2*n 타일에서 1개가 늘어나면 2*1짜리 타일 하나만 추가할 수 있고,
# 2개가 늘어나면 1*2타일 2개를 붙이거나, 2*2타일을 붙일 수 있으므로 두 가지 방법에 대해 x2를 해준다.
# 따라서 점화식은 dp[n] = dp[n-1] + 2*dp[n-2]