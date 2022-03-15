from collections import deque

n,w,l=map(int,input().split())
truck=deque(list(map(int,input().split()))) # deque에 트럭 무게 입력

ans_time=0
bridge=deque([0]*w)         # 다리의 길이만큼 deque 선언 및 초기화

while truck:       # 트럭이 다 지나갈때까지 반복
    bridge.popleft()    # 맨 앞 트럭 pop(지나감을 의미)

    if len(bridge)<w:    # 다리 위에 있는 원소가 w(다리길이) 보다 적은 경우,
        if sum(bridge)+truck[0]<=l:     # 다리위 무게+진입할 트럭 무게 < L (최대하중) 이면,
            bridge.append(truck.popleft()) # 다리 list에 진입할 트럭 무게 append(추가)
        else:
            bridge.append(0)             # 합이 최대하중 보다 크면 다리 list에 0 append(=아무것도 추가x) 
    ans_time+=1

ans=ans_time+w      # while문에 마지막 트럭이 지나가는 경우가 포함되지 않았으므로 시간에 w만큼 더함
print(ans)