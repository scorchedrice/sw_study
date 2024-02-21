'''
색을 칠하고
R, B의 외각의 길이를 구한다 (내부제외)
이후 P의 외각 길이를 구해 더한다
'''
def count_color(i,j):
    now_i = i
    now_j = j
    cnt_i1 = 1
    cnt_i2 = 1
    cnt_j = 1
    while True:
        if now_i >= 9 or now_j >= 9:
            break
        if paper[now_i+1][j] == 1 or paper[now_i+1][j] == 2:
            cnt_i += 1
            now_i += 1
        else:
            break
    
    while True:
        if now_i >= 9 or now_j >= 9:
            break
        if paper[now_i][now_j+1] == 1 or paper[now_i][now_j] == 2:
            cnt_i += 1
            now_i += 1
        else:
            break
    
    while True:
        if now_j >= 10 or now_i >= 10:
            break
        if paper[i][now_j+1] == 1 or paper[i][now_j+1] == 2:
            cnt_j += 1
            now_j += 1
        else:
            break

    for k in range(i,now_i+1):
        for l in range(j, now_j+1):
            paper[k][l] -= 2

    return 2*(now_i + now_j)


# T = int(input())
# for tc in range(1,T+1):
paper = [[0 for _ in range(10)] for _ in range(10)]
print(paper)
painting = int(input())
origin_len = []
paint_color = []
for _ in range(painting):
    Si,Sj,Ei,Ej,color = map(int,input().split())
    for i in range(Si,Ei+1):
        for j in range(Sj,Ej+1):
            paper[i][j] += color
    origin_len +=[2*((Ei-Si+1)+(Ej-Sj+1))]
    paint_color += [color]
for k in range(10):
    print(paper[k])

total = 0
for m in range(10):
    for n in range(10):
        if paper[m][n] == 1:
            total += count_color(m,n)
print(total)
for k in range(10):
    print(paper[k])
