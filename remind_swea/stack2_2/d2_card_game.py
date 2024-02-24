'''
i부터 j까지의 학생
group1 : i 이상 (i+j)//2 이하
group2 : (i+j)//2 + 1 이상 j이하
'''
def who_is_winner(a,b):
    if card[a] == card[b]:
        return a
    elif card[a] == 1 and card[b] == 2:
        return b
    elif card[a] == 1 and card[b] == 3:
        return a
    elif card[a] == 2 and card[b] == 1:
        return a
    elif card[a] == 2 and card[b] == 3:
        return b
    elif card[a] == 3 and card[b] == 1:
        return b
    elif card[a] == 3 and card[b] == 2:
        return a

def backtrace(a,b):
    if a == b:
        return a
    else:
        left = backtrace(a,(a+b)//2)
        right = backtrace((a+b)//2+1,b)
        return who_is_winner(left, right)

T = int(input())
for tc in range(1,T+1):

    N = int(input())
    card = list(map(int,input().split()))
    print(backtrace(0,N-1))