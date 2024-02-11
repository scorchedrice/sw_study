# 4871. 내가 실수한 내용이 무엇인가
def dfs(start_room):
    visited[start_room] = 1
    stack = []
    while True:
        for i in input_map_data[start_room]:
            if visited[i] == 0: # 방문한 경우가 없으면
                stack += [start_room] # stack에 해당하는 방 번호를 추가한다.
                start_room = i # 그 방으로 이동하고
                visited[i] = 1 # 방문 기록을 남긴다.
                break
       
        else: # for loop에 걸리지 않은 경우
            if stack == []:
                return visited[end_room]
            else:
                start_room = stack.pop()
    
T = int(input())
for tc in range(1, T+1):

    V, E = map(int, input().split()) # V의 방, E의 다리

    input_map_data = [[] for _ in range(V+1)] # 해당 방의 정보 반영위해
    visited = [0] * (V+1)
    for i in range(E):
        room_num, connect_room_num = map(int, input().split())
        input_map_data[room_num] += [connect_room_num]

    start_room, end_room = map(int, input().split())
    print(f"#{tc} {dfs(start_room)}")