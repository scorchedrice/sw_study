'''
1번부터 N번까지 N개의 상자
처음에는 모두 0이 적혀있음.

Q회동안 작업을 진행한다. 작업 내용은 다음과 같다.
" i번째 작업에 대해 L번 상자부터 R번 상자까지의 값을 i로 변경 "
Q회동안 작업을 한 후 N개의 상자에 적혀있는 값들을 순서대로 출력하는 프로그램 작성
'''

T = int(input())
for tc in range(1,T+1):
    N, Q = map(int, input().split())
    # N은 상자의 개수, Q는 작업 횟수

    box_change_range = [[]]
    for k in range(Q):
        box_change_range += [list(map(int,input().split()))]
    # 상자를 바꿀 범위를 담은 리스트 작성

    box_info = [0] * (N+1)
    # 상자 상태 초기화

    for step in range(1,Q+1):
        start = box_change_range[step][0]
        end = box_change_range[step][1]
        for numbering in range(start, end+1):
            box_info[numbering] = step
    box_info.pop(0)
    print(f"#{tc}", end = ' ')
    print(*box_info)
