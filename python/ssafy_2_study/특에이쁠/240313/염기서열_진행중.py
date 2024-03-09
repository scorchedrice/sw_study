from collections import deque

N, M = map(int,input().split())
dna_lst = deque()
for _ in range(N):
    dna_lst.append(input())

def mix_dna(dna1, dna2):
    mixed_dna = ''
    for i in range(M):
        if dna1[i] == dna2[i]:
            mixed_dna += dna1[i]
        elif dna1[i] == '.':
            mixed_dna += dna2[i]
        elif dna2[i] == '.':
            mixed_dna += dna1[i]
        else:
            return None
    return mixed_dna

def compress(lst):
    result = deque()
    while True:
        pivot1 = dna_lst.popleft()
        if dna_lst == deque():
            result.append(dna_lst)
            return result
        pivot2 = dna_lst.popleft()
        after_mix = mix_dna(pivot1, pivot2)
        if 
    