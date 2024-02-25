'''
가위1, 바위2, 보3
1,2 : b 
1,3 : a
2,1 : a
2,3 : b
3,1 : b
3,2 : a
'''

def winner(a,b):
    game = [card[a],card[b]]
    if card[a]==card[b] or game == [1,3] or game == [2,1] or game == [3,2]:
        return a
    else:
        return b

def backtrack(i,j):
    if i == j:
        return i
    else:
        left = backtrack(i,(i+j)//2)
        right = backtrack((i+j)//2+1,j)
        return winner(left,right)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    card = list(map(int,input().split()))
    print(f"#{tc} {backtrack(0,N-1)+1}")