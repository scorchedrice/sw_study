from copy import deepcopy

N = int(input())
order_lst = []
special_lst = []
time_set = set()
result = {}
tmp = 0
tmp_sec = 0
for _ in range(N):
    a, b = input().split()
    a = int(a)
    time_set.add(a)
    if b == 'A':
        b = 0
    elif b == 'B':
        b = 1
    elif b == 'C':
        b = 2
    elif b == 'D':
        b = 3
    if len(time_set) != tmp:
        special_lst.append([])
        tmp += 1
    special_lst[-1].append(b) # 해당 시간대에 어떤 교차로에 차량이 존재하는지
    order_lst.append((a,b)) # 추후 해당 시간대의 dict값을 불러오기 위함임.
time_lst = list(time_set)

def traffic(stage,time_idx):
    now_time = time_lst[time_idx]
    global result
    while True:
        if stage[0] != [] and stage[1] != [] and stage[2] != [] and stage[3] != []:
            return
        if stage == [[],[],[],[]]:
            return
        if 0<=time_idx+1<len(time_lst):
            if now_time == time_lst[time_idx+1]:
                return
        if stage[0] != [] and stage[3] == []:
            result[(stage[0].pop(0),0)] = now_time
        if stage[1] != [] and stage[0] == []:
            result[(stage[1].pop(0),1)] = now_time
        if stage[2] != [] and stage[1] == []:
            result[(stage[2].pop(0),2)] = now_time
        if stage[3] != [] and stage[2] == []:
            result[(stage[3].pop(0),3)] = now_time
        now_time += 1
        print(stage)
        print(result)

time_idx = 0
stage = [[],[],[],[]] # A,B,C,D
for k in range(len(time_lst)):
    target = special_lst[time_idx]
    for l in range(len(target)):
        stage[target[l]].append(time_lst[time_idx])
    traffic(stage,time_idx)
    time_idx += 1

print(time_lst)
print(special_lst)
print(stage)