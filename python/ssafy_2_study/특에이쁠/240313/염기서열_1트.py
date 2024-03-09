# 1/3 성공, 하나 시간초과
import sys
from copy import deepcopy
def check_same(word_lst):
    tmp = deepcopy(word_lst)
    while True:
        filter_dna = set()
        for i in range(len(word_lst)-1):
            word1 = word_lst[i]
            for j in range(i+1,len(word_lst)):
                word2 = word_lst[j]
                can_transform = True
                memory = ''
                for k in range(M):
                    if word1[k] == word2[k]:
                        memory += word1[k]
                    elif word1[k] == '.' and word2[k] != '.':
                        memory += word2[k]
                    elif word2[k] == '.' and word1[k] != '.':
                        memory += word1[k]
                    elif word1[k] == '.' and word2[k] == '.':
                        memory += '.'
                    else:
                        can_transform = False
                        break
                if can_transform == True:
                    filter_dna.add(memory)
        if filter_dna == set():
            return tmp
        else:
            tmp = deepcopy(list(filter_dna))
            word_lst = deepcopy(list(filter_dna))

N, M = map(int,input().split())
dna_lst = []
for _ in range(N):
    dna_lst.append(input())
print(len(check_same(dna_lst)))