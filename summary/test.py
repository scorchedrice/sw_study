'''
H행 W열, 동서남북
L : 왼쪽 90
R : 오른쪽 90
A : 두칸 전진 (방향유지), 단 idx 조건 내 인 경우만 시행
'''
'''
같은 칸 두번이상 방문 금지(visited 활용)
방문한 칸 표시

로봇이 방문한 칸은 3칸 이상
'''
from copy import deepcopy

# look-up table
dir_info = [0,1,2,3]
L_info = [3,0,1,2]
R_info = [1,2,3,0]

def dir_func(now_dir, target_dir):
    if L_info[now_dir] == target_dir:
        return 'L'
    elif R_info[now_dir] == target_dir:
        return 'R'

di = [-1,0,1,0] # 북 동 남 서
dj = [0,1,0,-1]

def dfs(ci,cj,lst,record,c_dir): # 명령어 저장 lst, 방문 칸 카운트 record
    global f_dir # 최초의 위치 설정 위함
    global mn # 최소 카운트인 경우 mn값에 명령 목록을 저장
    if record == pivot:
        if len(lst) < len(mn):
            mn = lst
        return
    if len(mn) < len(lst): # 최소 값보다 명령을 더 한 경우 더 연산할 필요성 없음.
        return
    
    cnt = deepcopy(lst)
    for dir in range(4):
        # 4방향 탐색 시작
        s_i = ci + di[dir]
        s_j = cj + di[dir]
        m_i = ci + 2*di[dir]
        m_j = cj + 2*dj[dir]
        # 한칸 이동한 경우 s, 두칸 이동한 경우 m, 둘다 조건을 만족해야함.
        if 0<=m_i<H and 0<=m_j<W and v[s_i][s_j] == '#' and v[m_i][m_j] == '#':
            # 인덱스를 만족하면서, s, m 모두 방문 기록이 없다면
            if record == 1: # 이제 명령을 받기 시작한 로봇이라면
                f_dir = dir # 일단 f_dir 값을 저장
                cnt += f_dir
            else: # 명령을 수행하고 있어 원래의 방향을 가지고 있다면
                if dir != c_dir: # 그 방향과 이 반복문에서 부여받은 방향이 다르다면
                    dir_memory = dir_func(c_dir, dir)
                    cnt += dir_memory
            
            # 이제 전진이 가능한 조건을 모두 충족했으니, A를 append하고 record 값을 수정한다.
            cnt += 'A'
            v[m_i][m_j] = '.'
            v[s_i][s_j] = '.' # 방문 기록
            dfs(m_i, m_j, cnt, record + 2, dir)
            v[m_i][m_j] = '#'
            v[s_i][s_j] = '#' # 방문 기록되돌리고 다음 반복문 진행
      

H, W = map(int,input().split())
matrix = []
pre_v = []
pivot = 0
for _ in range(H):
    lst = list(input())
    for k in range(W):
        if lst[k] == '#':
            pre_v.append((_,k))
            pivot += 1
    matrix.append(lst)
mn = [0] * 987654321
for i in range(len(pre_v)):
    f_dir = 0
    v = deepcopy(matrix)
    now_i = pre_v[i][0]
    now_j = pre_v[i][1]
    v[now_i][now_j] = '.'
    dfs(now_i, now_j, '', 1, 0)
    print(mn)
print(mn)