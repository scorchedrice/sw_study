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

direct_info = [0, 1, 2, 3] 
# 서로 시작하면 3, 2, 1, 0 순으로 방향을 바꾼다.
# 마찬가지로 동으로 시작하면 1, 0, 3, 2 로 방향을 바꾼다.
# 즉 index 가 하나씩 줄어든다고 보면 된다. (서로 시작하는 경우 3, 2, 1, 0으로 direct_info index가 바뀌고 동으로 시작하는 경우 1, 0, -1, -2로 direct_info index가 바뀐다.)

def find_dir_index(d): # direct_info에서 index를 추출
    for index in range(0, len(direct_info)):
        if direct_info[index] == d:
            return index
