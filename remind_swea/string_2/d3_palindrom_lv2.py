# size는 8*8
# 고려해야 할 단어 길이는 3,4,5,6,7,8
'''
가로 혹은 세로만 고려하면 되기에
각 단어 길이 규격에 맞춰 하나씩 비교해보고
회문 여부를 판단하자
'''
'''
i(행, 가로)를 고려할 때, index 0부터 8-size까지 고려하면 된다
j또한 마찬가지
'''
def find_palindrome_i(i, N):
    size = N
    max_index = 8-N
    cnt = 0
    for k in range(0,max_index+1):
        check_str = matrix[i][k:k+N]
        if check_str == list(reversed(check_str)):
            cnt += 1
    return cnt

def find_palindrome_j(j,N):
    size = N
    max_index = 8-N
    cnt = 0
    for k in range(0,max_index+1):
        check_str = []
        for l in range(N):
            check_str += [matrix[k+l][j]]
        if check_str == list(reversed(check_str)):
            cnt += 1
    return cnt
for tc in range(1,11):
    N = int(input())
    matrix = []
    total = 0
    for _ in range(8):
        matrix += [list(input())]

    for i in range(8):
        total += find_palindrome_i(i,N)
        total += find_palindrome_j(i,N)

    print(f"#{tc} {total}")

