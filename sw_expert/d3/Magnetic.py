# 파란색 : N극에 끌림 (S), 붉은색 : S극에 끌림 (N)
# 자성체는 테이블에 있는 N,S극에만 반응한다. (자기들끼리 반응 없음)
# 1은 N극의 성질을 가지는 자성체(붉은색, 아래이동), 2는 S극의 성질을 가지는 자성체(파란색, 위로이동)
# 테이블의 크기는 100*100 으로 고정
# testcase는 10

'''
상단을 N, 하단을 S라고 한다면
하나하나 이동 가능 여부를 판단하고 이동한다.
이 때, 가야하는 방향이 달라 충돌한다면 이동을 멈춘다.

생각해보니까, 중력문제와 비슷하게 풀이할 수 있을 것 같음.
일단 교착상태의 수를 구하는 것이 목적이니.
하단에 있는 1을 제거하고 1들을 아래로 이동시킨다. (조건을 2를 만난 경우 멈춘다로 두고)
어차피 위로 방해없이 이동 할 수 있는 애들은 1에 걸림이 없이 올라간다는 말과 동일하므로 고려할 필요 없음
하단 1 제거, 이동, 하단 1 제거, 이동 이 과정을 반복하면 어느 순간 변화가 없는데
변화가 없을 때 루프를 중단시키는 조건을 추가해 최종 map을 구한다.
'''

'''
교착단계의 수를 판단할 땐, 한 열씩 본다.
아래로 가고자 하는 것(1), 위로 가고자 하는 것(2)의 충돌 한 쌍의 개수가 교착단계의 수와 동일하다.
'''
def remove_magnetic(table_matrix):
    for num1 in range(100):
        if table_matrix[99][num1] == 1: # 마지막 줄에 1이 있다면
            table_matrix[99][num1] = 0 # 제거
    return

def move_magnetic(table_matrix):
    while True:
        move_cnt = 0
        # 우선 아래로 이동하는 '1'은 아래부터 이동시키고 (하단부터 작업시작)
        for i in range(98, -1, -1):
            for j in range(100):
                if table_matrix[i][j] == 1 and table_matrix[i+1][j] != 2:
                    # 해당 위치에 1이 있고 그 아래에 2가 없다면(이동 가능하다면)
                    table_matrix[i][j] = 0
                    table_matrix[i+1][j] = 1
                    move_cnt += 1
        remove_magnetic(table_matrix) # 모두 이동 시킨 후 사이드 제거 작업 진행

        if move_cnt == 0: # 변화를 준 이후 그게 직전 매트릭스와 차이가 없다면
            print('break')
            return

def cnt_break(table_matrix):
    result = 0
    for j in range(100):
        for i in range(99):
            # j 열을 확인
            if table_matrix[i][j] == 1 and table_matrix[i+1][j] == 2:
                # 아래로 가는 1과 위로가는 2가 붙어있다면
                result += 1
    return result

for tc in range(1, 11):
    N = int(input()) # 항상 100

    table_matrix = [list(map(int, input().split())) for _ in range(100)] # table_matrix 작성
    move_magnetic(table_matrix)
    cnt_break(table_matrix)
    print(f"#{tc} {cnt_break(table_matrix)}")