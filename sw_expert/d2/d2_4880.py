# 토너먼트 카드게임
# 1 : 찌
# 2 : 묵
# 3 : 빠
# 1,2 : 2승 | 1,3 : 1승 | 2,3 : 3승
# 같은 것을 내면 숫자가 작은 쪽이 승리
def winner(a,b):
    if [a,b] == [2,1] or [a,b] == [1,3] or [a,b] == [3,2] or a == b:
        return a
    else:
        return b

def div(i,j):
    if i == j:
        return i
    else:
        left = div(i,(i+j)//2)
        right = div((i+j)//2 +1, j)
    return winner(left,right)
    
T = int(input())
for tc in range(1,1+T):
    N = int(input())
    student_card = [0] + list(map(int, input().split()))
    print(f"#{tc} {div(1,N)}")