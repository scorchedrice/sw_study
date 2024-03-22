import sys
'''
초반에 불필요한 과정이 있었음. 이러한 과정 없이 진행하는 연습 필요 (special_lst 불필요)
'''
def traffic_rule(car_lst): # 교차로 현황에 따른 이동 가능한 차량 출력 함수
    if len(car_lst) == 1:
        return [car_lst[0]]
    elif len(car_lst) == 2:
        if car_lst[0][0] == 0: #A
            if car_lst[1][0] == 1: # A, B
                return [car_lst[0]]
            elif car_lst[1][0] == 2: # A, C
                return [car_lst[0],car_lst[1]]
            else: # A, D
                return [car_lst[1]]
        elif car_lst[0][0] == 1: # B
            if car_lst[1][0] == 2: # BC
                return [car_lst[0]]
            elif car_lst[1][0] == 3: # BD
                return [car_lst[0],car_lst[1]]
        elif car_lst[0][0] == 2: # C
            if car_lst[1][0] == 3: # CD
                return [car_lst[0]]
    elif len(car_lst) == 3:
        if car_lst[0][0] == 0:
            if car_lst[1][0] == 1 and car_lst[2][0] == 2: # ABC
                return [car_lst[0]]
            elif car_lst[1][0] == 1 and car_lst[2][0] == 3: # ABD
                return [car_lst[2]]
            elif car_lst[1][0] == 2 and car_lst[2][0] == 3: # ACD
                return [car_lst[1]]
        elif car_lst[0][0] == 1: # BCD
            return [car_lst[0]]
    elif len(car_lst) == 4:
        return False
    else:
        return None

N = int(input())
order_lst = [] # 추후 이 리스트를 기반으로 dict에서 뽑아서 출력할 예정
special_lst = [] # 시간대 별 교차로 정보를 반영하기 위함
time_set = set() # 입력 값의 시간들을 정리해서 넓은 범위의 시간을 하나하나 탐색하는 경우를 방지하기 위함.
result = {} # 결과값을 입력할 딕셔너리
tmp = 0
# tmp_sec = 0
for _ in range(N):
    a, b = input().split()
    a = int(a)
    time_set.add(a) # 시간대 정보 입력
    if b == 'A': # 방향 정보를 숫자 정보로 전환
        b = 0
    elif b == 'B':
        b = 1
    elif b == 'C':
        b = 2
    elif b == 'D':
        b = 3
    if len(time_set) != tmp: # tmp와 다르다 == 새로운 시간값이 추가 된 것
        special_lst.append([]) # 그러면 새로운 빈 리스트를 추가함 (시간 추가된 만큼 추가하기 위함)
        tmp += 1 # 새로운 시간 값이 추가 되었다 == 시간 정보가 하나 증가했다.
    special_lst[-1].append(b) # 해당 시간대에 어떤 교차로에 차량이 존재하는지, 최근 추가한 빈 리스트에 반영
    order_lst.append((b,a)) # 추후 해당 시간대의 dict값을 불러오기 위함임. (구역, 시간)

# 아래는 교차로 별 어떤 정보의 차량이 대기하고 있는지 작성하기 위한 과정
time_lst = list(time_set) # set값을 활용하기 위해 리스트 전환
time_idx = 0
# weight = 0
stage = [[],[],[],[]] # A,B,C,D
for k in range(len(time_lst)):
    target = special_lst[time_idx] # 시간대 별로 하나하나 보면서, 시간 순으로 누적시키는 과정
    # 사실 order_lst 그대로 사용해도 괜찮을 듯 하나, 문제풀이 당시 생각을 이렇게 했음.
    for l in range(len(target)):
        stage[target[l]].append(time_lst[time_idx])
    # print('Stage',stage)
    time_idx += 1 # 해당 시간대에 누적을 마무리 했다면, 그 다음 시간대의 차량을 누적
# print('STAGE',stage)


current = time_lst[0] # 현재 시간을 시간 정보 리스트의 최솟값으로 할당하고
current_idx = 0 # 추후 이 인덱스를 늘려가며 차량 통행이 없는 일정 시간대를 스킵하는 과정에 활용
# print(current)
# print(time_lst)
KK = len(time_lst)
while stage != [[],[],[],[]]: # stage(교차로 현황)가 비지 않았다면 반복
    # print('CURRENT',current)
    car_lst = []
    for k in range(4): # 교차로 A,B,C,D를 탐색
        if stage[k] != [] and stage[k][0] <= current: # 비어있지 않고, 해당 구역 맨 앞 차량 정보가 현 시간 이하 시간값이라면
            car_lst.append((k,stage[k][0])) # 차량 정보를 업데이트 (교통정리를 위한 임시)
    pivot = traffic_rule(car_lst) # 교통정리 함수 결과를 pivot에 할당하고 아래의 과정을 통해 추가 작업 진행
    if pivot == False: # 교착상태, 더 이상 나갈 수 없는 상태.
        break
    elif pivot != None: # 무언가 결과가 나온 상태로 이 값들에 시간값들을 할당한다.
        # print('PIVOT',pivot)
        for k in range(len(pivot)):
            stage[pivot[k][0]].pop(0)
            result[pivot[k]] = current
        current += 1
    elif pivot == None: # 현 시간대로는 뺼 수 있는 것이 없는 상태로 이 시간을 기준으로 가장 가까운 미래 시간대로 시간을 변경한다.
        while True:
            current_idx += 1 # idx를 바꿔가며 시간값을 찾는다.
            if time_lst[current_idx] >= current:
                current = time_lst[current_idx]
                break
            else:
                continue
        
last_check = result.keys() # 딕셔너리 키에 이 값이 존재한다면 출력한다.
for a in range(N):
    if order_lst[a] in last_check:
        print(result[order_lst[a]])
    else:
        print('-1')
