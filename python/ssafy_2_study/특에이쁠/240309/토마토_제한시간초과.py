'''
리스트로 익은 토마토의 정보를 받고, 이를 익지않은 토마토 좌표와 비교하는 과정을 통해 해결하려 했다.
하지만, matrix를 설정하는 것 보다 이 과정이 더 시간이 오래 걸렸던 것 같다.
아무래도 리스트를 계속 반복하는 과정이 쌓여, 복잡도가 올라간 듯 하다.
'''

from copy import deepcopy

length, width, height = map(int,input().split())
tmt = []
v = []
for k in range(height):
    for i in range(width):
        tmt_lst = list(map(int,input().split()))
        for j in range(length):
            if tmt_lst[j] == 0:
                tmt.append((j,i,k))
                v.append(0)
            elif tmt_lst[j] == 1:
                tmt.append((j,i,k))
                v.append(1)

pivot = [1] * len(v)
cnt = 0
possible = True
while v != pivot:
    tmp = deepcopy(v)
    for i in range(len(tmt)):
        if tmp[i] == 1:
            rx, ry, rz = tmt[i]
            for j in range(len(tmt)-1, -1, -1):
                if v[j] == 0:
                    ux,uy,uz = tmt[j]
                    if abs(rx-ux) + abs(ry-uy) + abs(rz-uz) == 1:
                        v[j] = 1
    if tmp == v:
        possible = False
        break
    cnt += 1
    
if possible == True:
    print(cnt)
elif possible == False:
    print('-1')