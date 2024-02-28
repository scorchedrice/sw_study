'''
구슬 쏘기 : N번
벽돌 정보 : W(가로) * H(세로) 배열, 가로세로 주의!!!!

벽돌은 숫자로 표시된다.
구슬은 좌우로만 움직일 수 있다. 항상 맨위의 벽돌만 깬다.
구슬이 적중하면, 상하좌우로 (벽돌에 적힌 수 -1 범위) 제거된다.
영향 받은 모든 벽돌은 동일한 규칙을 적용받는다.
'''

'''
정의할 함수
- 깨진 벽돌이 몇개인지 판단하는 함수
- 구슬 쏘는 횟수만큼 경우의 수를 돌려보는 재귀를 활용한 함수
'''
di = [-1,1,0,0] #상하좌우
dj = [0,0,-1,1]

def count_brick(matrix):
    cnt = 0
    for i in range(H):
        for j in range(W):
            if matrix[i][j] != 0:
                cnt += 1
    return cnt

def top_brick(matrix):
    result = []
    for j in range(W):
        for i in range(H):
            if matrix[i][j] != 0:
                result += [(i,j)]
                break
    return result

def gravity(matrix):
    after_shoot = [[0 for _ in range(W)] for _ in range(H)]
    for j in range(W):
        memory = []
        for i in range(H-1,-1,-1):
            if matrix[i][j] != 0:
                memory += [matrix[i][j]]
        for k in range(H-1, H-1-len(memory), -1):
            after_shoot[k][j] = memory[H-k-1]
    return after_shoot

def break_brick(now_i,now_j,matrix):
    while True:
        if matrix[now_i][now_j] == 0:
            return matrix
        # if matrix[now_i][now_j] == 1:
        #     matrix[now_i][now_j] = 0
        #     return
        elif matrix[now_i][now_j] >= 1:
            alpha = matrix[now_i][now_j]
            matrix[now_i][now_j] = 0
            for bonus in range(1,alpha):
                for dir in range(4):
                    move_i = now_i + di[dir]*(bonus)
                    move_j = now_j + dj[dir]*(bonus)
                    if 0<=move_i<=W-1 and 0<=move_j<=H-1:
                        if matrix[move_i][move_j] == 1:
                            matrix[move_i][move_j] = 0
                        elif matrix[move_i][move_j] >= 2:
                            break_brick(move_i, move_j, matrix)
                            matrix[move_i][move_j] = 0
                        
def game_start(matrix):
    result = []
    target = top_brick(matrix)
    origin_matrix = []
    origin_matrix += matrix
    for k in target:
        

# T = int(input())
# for tc in range(1,T+1):
N, W, H = map(int,input().split())
# N 구슬쏘는횟수, W 가로(j), H 세로(i)
matrix = []
for i in range(H):
    matrix += [list(map(int,input().split()))]
origin_brick = count_brick(matrix)
