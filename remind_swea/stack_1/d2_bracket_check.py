T=int(input())
for tc in range(1,T+1):
 
    check_str = input()
    stack = []
    result = 1
    for k in range(len(check_str)):
        if check_str[k] == '{' or check_str[k] == '(':
            stack += [check_str[k]]
        elif (check_str[k] == '}' or check_str[k] == ')') and stack == []:
            result = 0
            break
        elif check_str[k] == '}' and stack[-1] == '{':
            stack.pop()
        elif check_str[k] == '}' and (stack[-1] != '{'):
            result = 0
            break
        elif check_str[k] == ')' and stack[-1] == '(':
            stack.pop()
        elif check_str[k] == ')' and (stack[-1] != '('):
            result = 0
            break
    if stack != []:
        result = 0
 
    print(f"#{tc} {result}")