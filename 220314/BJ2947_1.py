lst=list(map(int,input().split()))

while True:
    if lst[0]>lst[1]:
        lst[0],lst[1]=lst[1],lst[0]
        print(*lst)
    if lst[1]>lst[2]:
        lst[1],lst[2]=lst[2],lst[1]
        print(*lst)
    if lst[2]>lst[3]:
        lst[2],lst[3]=lst[3],lst[2]
        print(*lst)
    if lst[3]>lst[4]:
        lst[3],lst[4]=lst[4],lst[3]
        print(*lst)
    
    if lst==sorted(lst):
        break

# 문제에서 주어진 조건대로 전부 조건문을 작성하고 반복문을 돌린 풀이