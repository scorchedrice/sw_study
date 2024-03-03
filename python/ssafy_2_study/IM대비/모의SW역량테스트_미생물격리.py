'''
정사각형 영역 (N x N)
바깥 쪽에는 특수처리 (미생물들의 구역 벗어나는 것을 방지)

미생물은 상하좌우로 이동한다.
미생물 군집 시작 위치, 군집 내 미생물 마리수, 이동방향이 주어진다.
'''
'''
한시간마다 군집은 이동한다.
특수처리 구역에 도달하면, 다음과 같은 현상이 발생한다.
    1. 군집 내 마리수 = int(군집 내 마리수/2)
    2. 이동 방향이 반대로 전환됨
더불어, 군집간 좌표가 겹치는 경우 합쳐진 이후 미생물 수 가 많은 군집의 방향으로 이동하게된다.
    # 마리수를 맨처음으로 하는 리스트 생성후 활용하기
M시간 미생물 군집 격리 후 남아있는 미생물의 총 수는?
'''
'''
1. 미생물 좌표 이동
    해당 좌표가 외각이라면 (i == 0 or j == 0)
        미생물 마리수 반토막
2. 이동 후 동일한 좌표가 있는지 확인한다.
    이 때 동일한 좌표가 있다면, 마리수를 합친 후 이를 비교해서 우세한 군집의 방향성을 부여한다.
3. 미생물이 모두 사라진다면 M이 되기 전에 이를 종료하고
    모두 사라지지 않는다면, M초 후 결과를 도출한다.
'''
dir = [0,(-1,0),(1,0),(0,-1),(0,1)] # 상하좌우

T = int(input())
for tc in range(1,T+1):
    N, M, K = map(int,input().split())
    # N은 격리 공간의 크기
    # M은 격리 시간
    # K는 미생물 군집의 개수
    mic_lst = []
    for _ in range(K):
        mic_i, mic_j, mic_num, mic_dir = map(int,input().split())
        mic_lst.append([mic_num, mic_i, mic_j, mic_dir])

    t = 0
    while True:
        if mic_lst == [] or t == M:
            break
        # 1. 미생물의 이동
        for k in range(len(mic_lst)):
            dir_info = mic_lst[k][3]
            mic_lst[k][1] = mic_lst[k][1] + dir[dir_info][0]
            mic_lst[k][2] = mic_lst[k][2] + dir[dir_info][1]
            # 특수처리 구역이라면, 군집 개채수 절반, 방향 전환
            if mic_lst[k][1] == 0 or mic_lst[k][2] == 0 or mic_lst[k][1] == N-1 or mic_lst[k][2] == N-1:
                mic_lst[k][0] = int(mic_lst[k][0]/2)
                if mic_lst[k][3] == 1:
                    mic_lst[k][3] = 2
                elif mic_lst[k][3] == 2:
                    mic_lst[k][3] = 1
                elif mic_lst[k][3] == 3:
                    mic_lst[k][3] = 4
                elif mic_lst[k][3] == 4:
                    mic_lst[k][3] = 3
        # 2. 동일한 좌표 확인 - 군집 통합 할 것이냐 말것이냐 결정
        visited = set()
        del_mic = set()
        for l in range(len(mic_lst)):
            ci = mic_lst[l][1]
            cj = mic_lst[l][2]
            if (ci,cj) in visited:
                del_mic.add((ci,cj))
            else:
                visited.add((ci,cj))
        # print(del_mic)
        # 군집 통합과정 진행
        del_mic = list(del_mic)
        for d in range(len(del_mic)):
            memory = []
            for s in range(len(mic_lst)-1,-1,-1):
                if mic_lst[s][0] == 0:
                    del mic_lst[s]
                    continue
                if (mic_lst[s][1], mic_lst[s][2]) == del_mic[d]:
                    memory.append(mic_lst[s])
                    del mic_lst[s]
            if memory != []:
                memory.sort(reverse = True)
                det_dir = memory[0][3]
                sum_mic = 0
                for m in range(len(memory)):
                    sum_mic += memory[m][0]
                mic_lst.append([sum_mic, del_mic[d][0], del_mic[d][1], det_dir])
        t += 1
    result = 0
    for k in range(len(mic_lst)):
        result += mic_lst[k][0]
    print(f"#{tc} {result}")