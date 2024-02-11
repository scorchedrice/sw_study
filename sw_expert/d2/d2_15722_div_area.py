# N*N table
# N은 2이상 20이하의 정수

# 가로선 : 0이상 i미만, i이상 N-1이하 범위로 구분한다.
'''
가로선의 범위 : 1~N-2
가로선이 3이라고 한다면 (0,1,2) | (3,4, ... N-1)
'''
# 세로선 : 0이상 i미만, i이상 N-1이하 범위로 구분한다.
'''
세로선의 범위 1~N-1
세로선이 5라고 한다면 (0,1,2,3,4) | (5,6,7 ... N-1)
'''
# 가로선과 세로선을 모두 고려할 때
'''
만약 가로선 A, 세로선 B라고 한다면
1 2
3 4
sector 1 i : [0:A] j : [0:B]
sector 2 i : [0:A] j : [B:N]
sector 3 i : [A:N] j : [0:B]
sector 4 i : [A:N] j : [B:N]
'''

T = int(input())
for tc in range(1,T+1):

    N = int(input())
    num_map = []
    for _ in range(N): # 숫자 배열 작성
        num_map += [list(map(int, input().split()))]

    result_list = []
    for A in range(1,N):
        for B in range(1,N): # 선을 긋고
            sector1 = 0
            sector2 = 0
            sector3 = 0
            sector4 = 0
            for i in range(A):
                for j in range(B):
                    sector1 += num_map[i][j]
            for m in range(A):
                for n in range(B, N):
                    sector2 += num_map[m][n]
            for q in range(A, N):
                for w in range(B):
                    sector3 += num_map[q][w]
            for k in range(A, N):
                for l in range(B, N):
                    sector4 += num_map[k][l]
            check_list = [sector1, sector2, sector3, sector4]
            result_list += [max(check_list) - min(check_list)]

    print(result_list)