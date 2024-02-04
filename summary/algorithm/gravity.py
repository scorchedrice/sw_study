'''
9
7 4 2 0 0 6 0 7 0
'''
N = int(input())
box_list = list(map(int, input().split()))

count_list = []
for i in range(N):
    count = 0
    for j in range(i+1, N):
        if box_list[i] > box_list[j]:
            count += 1
    count_list += [count]

print(max(count_list))