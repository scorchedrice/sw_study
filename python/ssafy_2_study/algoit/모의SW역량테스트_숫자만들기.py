from collections import deque

def append_oper(lst):
    oper_lst = ['+', '-', '*', '/']
    for i in range(4):
        if lst[i] != 0:
            for _ in range(lst[i]):
                oper.append(oper_lst[i])

def mix_oper(n,lst):
    if n == len(oper):
        oper_lst.append(lst)
        return
    prev = 0
    for i in range(N-1):
        if visited[i] == 0 and prev != oper[i]:
            prev = oper[i]
            visited[i] = 1
            mix_oper(n+1,lst+[oper[i]])
            visited[i] = 0

def my_cal(oper,num_list):
    result = num_list.popleft()
    while True:
        if num_list == deque():
            break
        OPER = oper.popleft()
        if OPER == '+':
            result = result + num_list.popleft()
        elif OPER == '-':
            result = result - num_list.popleft()
        elif OPER == '*':
            result = result * num_list.popleft()
        elif OPER == '/':
            result = int(result/num_list.popleft())
    return result

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    oper = []
    append_oper(list(map(int,input().split())))
    visited = [0] * (N-1)
    oper_lst = []
    mix_oper(0,[])
    num_list = deque(list(map(int,input().split())))
    prev = deque()
    for i in range(N):
        prev.append(num_list[i])

    max_cal = -987654321
    min_cal = 987654321
    for k in range(len(oper_lst)):
        use_oper = deque(oper_lst[k])
        after_cal = my_cal(use_oper,num_list)
        if after_cal > max_cal:
            max_cal = after_cal
        if after_cal < min_cal:
            min_cal = after_cal
        num_list += prev
    print(f"#{tc} {max_cal - min_cal}")