# 방을 작은 번호의 방에서 갈 뿐 아니라 큰 번호의 방에서도 간다.
'''
출발할 방 리스트
복도 리스트
도착할 방 리스트
이렇게 작성한 후에, 도착할 방 리스트 상단에 출발할 인원을 위치시켰을 때
다음 인원이 막혀서 갈 수 없다면, 기다렸다가 출발!
'''
def change_index(room):
    return (room-1)//2

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    top = list(range(1,400,2))
    hall = [0] * 200
    bottom = list(range(2,401,2))
    # top(홀수방) room, bottom(짝수방) room 관계
    # top_index = (room+1)/2 - 1
    # bottom_index = room/2 - 1
    for i in range(N):
        start, end = map(int,input().split())
        start_index = change_index(start)
        end_index = change_index(end)
        if start_index < end_index:    
            for i in range(start_index, end_index+1):
                hall[i] += 1
        elif start_index > end_index:
            for i in range(start_index, end_index-1, -1):
                hall[i] += 1
        
    cnt = 0
    while True:
        cnt += 1
        for i in range(200):
            if hall[i] > 0:
                hall[i] -= 1
        if hall == [0] * 200:
            break
    print(f"#{tc} {cnt}")