def change_str(input_str):
    stack = [input_str[0]]
    for i in range(1,len(input_str)):
        if stack == []:
            stack += input_str[i]
        elif stack[-1] == input_str[i]:
            stack.pop()
        else:
            stack += input_str[i]
        
    return len(stack)

T = int(input())
for tc in range(1,T+1):
    input_str = input()
    print(f"#{tc} {change_str(input_str)}")