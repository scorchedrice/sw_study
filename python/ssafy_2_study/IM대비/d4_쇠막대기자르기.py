def find_lazer(info):
    result = []
    for i in range(len(info)-1):
        if info[i] == '(' and info[i+1] == ')':
            info[i] = '-'
            info[i+1] = '-'
            result.append((i,i+1))
    return result

def find_blank(info):
    cnt = 0
    for i in range(len(info)-1):
        if info[i] == ')' and info[i+1] == '(':
            cnt += 1
    return cnt

def left_check(start_left):
    result = 0
    now = start_left
    while True:
        if now == 0:
            return result
        move = now - 1
        if info[move] == '(':
            result += 1
        elif info[move] == ')':
            result -= 1
        now = move
    
def right_check(start_right):
    result = 0
    now = start_right
    while True:
            if now == len(info)-1:
                return result
            move = now + 1
            if info[move] == ')':
                result += 1
            elif info[move] == '(':
                result -= 1
            now = move

def numbering(arr):
    result = arr[0][0]
    for k in range(num_lazer - 1):
        append_data = max(arr[k][1], arr[k+1][0])
        result += append_data
    result += arr[num_lazer-1][1]
    return result

T = int(input())
for tc in range(1,T+1):
    info = list(input())
    lazer_index = find_lazer(info)
    num_lazer = len(lazer_index)
    num_blank = find_blank(info)
    result = []
    for _ in range(num_lazer):
        left_lazer = lazer_index[_][0]
        right_lazer = lazer_index[_][1]
        result.append([left_check(left_lazer), right_check(right_lazer)])
    print(f"#{tc} {numbering(result) + num_blank}")
