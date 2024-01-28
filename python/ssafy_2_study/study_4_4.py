# 현민이의 게임개발
# 캐릭터의 위치 (A,B) .. A : 북쪽으로 부터 떨어진, B : 서쪽으로 부터 떨어진 칸의 개수
# 육지칸에서만 이동 가능
# 1. 현재 위치, 방향에서 왼쪽방향부터 갈 곳을 정한다
# 2. 왼쪽 방향의 칸에 가보지 않은 칸 존재시 그곳으로 한칸 전진, 가본 칸이라면 회전만하고 다음 과정 진행
# 3. 네 방향 모두 가본 칸 혹은 바다인경우 한 칸 뒤로가고(방향유지) 1단계로 돌아간다. 단 이때 뒤쪽 방향이 바다인 칸이라도 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.

N, M = list(map(int, input().split())) # 맵 생성 사이즈 입력
A, B, d = list(map(int, input().split())) # 좌표 및 방향 입력
# 0 북, 1 동, 2 남, 3 서
total_map = []
for i in range(0, N): # 행(N) 만큼 열(M) 크기의 리스트 입력해야 N x M 사이즈의 맵 구현 가능
    total_map.append(list(map(int, input().split())))

# 맵의 외곽은 항상 바다이며 시작 지점은 항상 육지이다.

A_move = [-1, 0, 1, 0]
B_move = [0, 1, 0, -1]

def change_dir(d): # 방향을 바꿀 때 사용할 함수 정의
    current_dir = d - 1
    if current_dir == -1:
        current_dir = 3
    return current_dir

def max_move(): # 0의 개수를 세는 것으로 0의 개수 이상으로 이동할 순 없기에 이를 최대 이동값으로 정하고 후에 이만큼 loop
    num_zero = 0
    for i in range(0,len(total_map)):
        for j in range(0,len(total_map[i])):
            if total_map[i][j] == 0:
                num_zero += 1
    return num_zero

# 게임 시작

count = 0
max_move = max_move()

while count != max_move: # max move 이하인 경우 게속 loop
    d = change_dir(d) # 현재 방향에서 방향 전환 1회
    if total_map[A + A_move[d]][B + B_move[d]] == 1 or total_map[A + A_move[d]][B + B_move[d]] == 2: # 갈 수 없다면
        d = change_dir(d) # 방향전환 2회
        if total_map[A + A_move[d]][B + B_move[d]] == 1 or total_map[A + A_move[d]][B + B_move[d]] == 2: # 갈 수 없다면
            d = change_dir(d) # 방향전환 3회
            if total_map[A + A_move[d]][B + B_move[d]] == 1 or total_map[A + A_move[d]][B + B_move[d]] == 2: # 갈 수 없다면
                d = change_dir(d) # 방향전환 4회 (원래방향)
                if total_map[A + A_move[d]][B + B_move[d]] == 1 or total_map[A + A_move[d]][B + B_move[d]] == 2: # 방향을 한바퀴 돌렸지만 갈 수 없는 경우 .. 뒤로 한칸!
                    A = A + A_move[d-2] # 바라보는 방향의 반대방향으로 이동, 하지만 바라보는 방향은 바뀌지 않음
                    B = B + B_move[d-2]
                    if total_map[A][B] == 1: # 뒤로 가는 좌표에 바다가 있다면 loop 종료
                        break
                elif total_map[A + A_move[d]][B + B_move[d]] == 0:
                    A = A + A_move[d] # 해당 좌표로 이동
                    B = B + B_move[d]
                    count = count + 1 # 숫자 더하기 1
                    total_map[A][B] = 2 # 한번 가본 곳은 2로 표시
            elif total_map[A + A_move[d]][B + B_move[d]] == 0:
                A = A + A_move[d]
                B = B + B_move[d]
                count = count + 1
                total_map[A][B] = 2
        elif total_map[A + A_move[d]][B + B_move[d]] == 0:
            A = A + A_move[d]
            B = B + B_move[d]
            count = count + 1
            total_map[A][B] = 2
    elif total_map[A + A_move[d]][B + B_move[d]] == 0:
        A = A + A_move[d]
        B = B + B_move[d]
        count = count + 1
        total_map[A][B] = 2
print(count)