def check_i(paper):
    global cnt
    for i in range(9):
        for j in range(10):
            if paper[i][j] != paper[i+1][j]:
                if (paper[i][j] == 1 and paper[i+1][j] == 2) or (paper[i][j] == 2 and paper[i+1][j] == 1):
                    cnt += 2
                else:
                    cnt += 1
                
def check_j(paper):
    global cnt
    for j in range(9):
        for i in range(10):
            if paper[i][j] != paper[i][j+1]:
                if (paper[i][j] == 1 and paper[i][j+1] == 2) or (paper[i][j] == 2 and paper[i][j+1] == 1):
                    cnt += 2
                else:
                    cnt += 1

def check_outline(paper):
    global cnt
    for i in range(10):
        if paper[0][i] != 0:
            cnt += 1
        if paper[9][i] != 0:
            cnt += 1
        if paper[i][0] != 0:
            cnt += 1
        if paper[i][9] != 0:
            cnt += 1

T = int(input())
for tc in range(1,T+1):
    paper = [[0 for _ in range(10)] for _ in range(10)]
  
    N = int(input())
    for _ in range(N):
        start_i, start_j, end_i, end_j, color = map(int,input().split())
        for i in range(start_i, end_i + 1):
            for j in range(start_j, end_j + 1):
                paper[i][j] += color
                if paper[i][j] == 3:
                    paper[i][j] = 0

    cnt = 0
    check_i(paper)
    check_j(paper)
    check_outline(paper)
    print(f"#{tc} {cnt}")