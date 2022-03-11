def solution(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 4
    else:
        return solution(n-3)+solution(n-2)+solution(n-1)

t=int(input())
for _ in range(t):
    n=int(input())
    print(solution(n))

# dp문제
# 첫번째 풀이와 달리 점화식을 list에 넣어주지 않고 함수로 해결
# sol함수에서 if문을 통해 n=1,2,3인 경우는 직접, 그 외에는 점화식으로 재귀함수를 적용한다.