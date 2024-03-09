# 개념 이해 필요. 못,, 못해!
# 5정답, 나머지 시간초과, 반례 틀림
# bit 활용하려 시도
'''
5 5
a....
aac..
aa.t.
aat..
a.cc.
'''

from sys import stdin
from collections import deque
from copy import deepcopy

N, M = map(int, stdin.readline().split())
dna_lst = []
for _ in range(N):
    dna_lst.append(input())

superDna_lst = []

def gen_bit(idx, size):
    pivot = list(bin(idx)[2:])
    for _ in range(len(pivot)):
        pivot[_] = int(pivot[_])
    return [0] * (size-len(pivot)) + pivot

def mix_dna(dna1, dna2):
    result = ''
    for i in range(M):
        if dna1[i] == '.' and dna2[i] != '.':
            result += dna2[i]
        elif dna2[i] == '.' and dna1[i] != '.':
            result += dna1[i]
        elif dna1[i] == dna2[i]:
            result += dna1[i]
        else:
            return []
    return result

def merge_dna(bit_info):
    merge_lst = []
    for i in range(N):
        if bit_info[i] == 1:
            merge_lst.append(dna_lst[i])
    if len(merge_lst) == 1: # 하나만 포함한다면, 통합과정 필요 없음
        return merge_lst
    else:
        merge_lst = deque(merge_lst)
        while True:
            if len(merge_lst) == 1:
                break
            dna1 = merge_lst.popleft()
            dna2 = merge_lst.popleft()
            after_mix = mix_dna(dna1, dna2)
            if after_mix == []:
                return []
            else:
                merge_lst.appendleft(after_mix)
        
        return list(merge_lst)

for i in range(1,2**N):
    idx = gen_bit(i, N)
    pivot = merge_dna(idx)
    if pivot != []:
        superDna_lst.append(pivot)
        
def match_dna(dna, dna_lst):
    global v
    for i in range(N):
        target = dna_lst[i]
        if v[i] == 0:
            for j in range(M):
                if target[j] == dna[j]:
                    continue
                elif target[j] == '.' and dna[j] != '.':
                    continue
                elif dna[j] == '.' and target[j] != '.':
                    continue
                else:
                    break
            else:
                v[i] = 1
    return

def check_possible(idx):
    global min_cnt
    global cnt
    global v
    cnt = 0
    candidate_len = len(idx)
    for i in range(candidate_len):
        if idx[i] == 1:
            pivot = superDna_lst[i][0]
            match_dna(pivot, dna_lst)
            cnt += 1
            if v == [1] * N:
                break
            if cnt > min_cnt:
                cnt = 0
                return
        else:
            continue
    if v == [1] * N:
        if min_cnt > cnt:
            min_cnt = cnt
            return

cnt = 0
min_cnt = 999
for j in range(2**len(superDna_lst)):
    v = [0] * (N)
    idx = gen_bit(j, len(superDna_lst))
    check_possible(idx)
print(min_cnt)