T = int(input())
for tc in range(1,T+1):
    info = list(input())
    stack = []
    result = 0
    for i in range(len(info)):
        if info[i] == '(':
            stack.append('(')
        elif info[i] == ')':
            if info[i-1] == '(': #레이저
                stack.pop()
                result += len(stack)
            else:
                result += 1
                stack.pop()
    print(f"#{tc} {result}")
