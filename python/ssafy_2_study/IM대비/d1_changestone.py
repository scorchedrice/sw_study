'''
i번째 돌을 사이에 두고 마주보는 j개의 돌에 대해
같은 색이면 뒤집고 다른색이면 그대로 둔다. (즉 j개의 돌에 대해 다른색으로 만든다.)
주어지는 돌을 벗어나는 경우엔 뒤집기 중단 (index 벗어나는 경우)
'''
def change(index):
    if stone[index] == 1:
        stone[index] -= 1
    elif stone[index] == 0:
        stone[index] += 1

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    # N : 돌의 개수, M : 작업 횟수
    stone = list(map(int,input().split()))
    for work in range(M):
        i, j = map(int,input().split())
        i = i-1
        
        for k in range(1,j+1):
            move_1 = i + k
            move_2 = i - k
            if 0<=move_1<=N-1 and 0<=move_2<=N-1:
                if stone[move_1] == stone[move_2]:
                    change(move_1)
                    change(move_2)
                else:
                    continue
            else:
                break
            
    print(f"#{tc}", end = ' ')
    print(*stone)
            