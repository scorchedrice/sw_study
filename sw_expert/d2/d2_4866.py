# {}, ()
def find_error(check_str):
    stack = [0]*len(check_str)
    top = -1
    for i in range(len(check_str)):

        if check_str[i] == '(':
            top += 1
            stack[top] = '('
            
        elif check_str[i] == '{':
            top += 1
            stack[top] = '{'
            
        elif check_str[i] == ')':
            if stack[top] == '(':
                stack[top] = 0
                top -= 1
                
            else:
                return 0
        elif check_str[i] == '}':
            if stack[top] == '{':
                stack[top] = 0
                top -= 1
                
            else:
                return 0
        else:
            continue
    
    if stack == [0]*len(check_str):
        return 1
    else:
        return 0
        


T = int(input())

for tc in range(1,T+1):
    check_str = input()
    print(f"#{tc} {find_error(check_str)}")