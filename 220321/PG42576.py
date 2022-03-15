
# 풀이1. 정답은 맞으나, remove함수 호출 시 for반복문에서 지속 호출되므로 효율성bad, 시간초과
def solution(participant, completion):
    answer = ''
    for compMan in completion:
        participant.remove(compMan)
    answer = participant[0]
    return answer


# 풀이2. 시간초과를 피하기 위해서 각 명단을 정렬한 뒤, 정렬된 명단 앞에서부터 두 명단을 index로 비교.
#        같지 않은 이름 있으면 해당 이름 return, 끝까지 가도 없으면 participant 마지막 원소 return 
def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    for i in range(len(participant)-1):
        if participant[i]!=completion[i]:
            return participant[i]
    answer=participant[-1]
    return answer


# 풀이2-1. 꼭 프로그래머스에서 기본적으로 주어진 answer return 형식으로 안해도 됨
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(participant)-1):
        if participant[i]!=completion[i]:
            return participant[i]
    return participant[-1]


# 풀이3. counter 이용. counter: 객체 자체를 뺄 수 있음. 두 명단을 통째로 처리 가능
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]