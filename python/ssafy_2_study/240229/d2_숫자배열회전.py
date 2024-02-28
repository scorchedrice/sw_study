def compress(matrix): # 매트릭스를 한 행씩 str으로 전환하는 함수
    result = []
    for i in range(N):
        result += [''.join(matrix[i])]
    return result
def change_90(matrix):
    result = []
    for j in range(N):
        memory=[]
        for i in range(N-1, -1, -1):
            memory += [matrix[i][j]]
        result += [memory]
    return result

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    matrix = []
    for _ in range(N):
        matrix += [list(input().split())]

    degree_90 = compress(change_90(matrix))
    degree_180 = compress(change_90(change_90(matrix)))
    degree_270 = compress(change_90(change_90(change_90(matrix))))
    print(f"#{tc}")
    for i in range(N):
        print(degree_90[i], end=' ')
        print(degree_180[i], end=' ')
        print(degree_270[i], end=' ')
        print()