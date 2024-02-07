# o321oo11o1o233o3
# ()(((()())(())()))(())

def cal_layer(stack): # 층수를 구하는 함수
    result = []
    for i in stack:
        if type(i) == int:
            result += [i]
    return max(result)

T = int(input())
for tc in range(1,T+1):
    pipe_info = list(input())
    # 레이저 위치를 o로 표시
    pipe_lazer = ['(']
    for i in range(1,len(pipe_info)):
        if pipe_lazer == []:
            pipe_lazer += pipe_info[i]
        elif pipe_lazer[-1] == '(' and pipe_info[i] == ')':
            pipe_lazer.pop()
            pipe_lazer += ['o']
        else:
            pipe_lazer += pipe_info[i]
    # 층 표시 (역순, 총 3층인 경우 3층은 1, 2층은 2, 1층은 3)
    layer_num = 1
    stack = [0]*len(pipe_lazer)
    top = -1
    for i in range(len(pipe_lazer)):
        if pipe_lazer[i] == 'o':
            top += 1
            stack[top] = 'o'
        elif pipe_lazer[i] == '(':
            top += 1
            stack[top] = layer_num
            layer_num += 1
        elif pipe_lazer[i] == ')':
            layer_num -= 1
            top += 1
            stack[top] = layer_num
            
    my_result = 0
    for k in range(cal_layer(stack), 0, -1):
        meet_k = 0
        my_cnt = 0
        for l in range(len(stack)):
            if stack[l] == k:
                meet_k += 1

            if meet_k % 2 == 1 and stack[l] == 'o':
                my_cnt += 1
            
            if meet_k % 2 == 0 and stack[l] == k:
                my_result += my_cnt + 1
                my_cnt = 0
            
    print(f"#{tc} {my_result}")
        
