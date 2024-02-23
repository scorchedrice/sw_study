def find_start(screen):
    for i in range(N):
        for j in range(M):
            if screen[i][j] == '1':
                return [i,j]

def find_end(screen):
    start_i = find_start(screen)[0]
    for j in range(M-1,-1,-1):
        if screen[start_i][j] == '1':
            return j

def div_secret_code(secret_code):
    result = []
    start = 0
    for k in range(8):
        result += [secret_code[start:start+7]]
        start += 7
    return result

def check_code(result):
    odd_sum = result[0]+result[2]+result[4]+result[6]
    even_sum = result[1]+result[3]+result[5]+result[7]
    if (odd_sum * 3 + even_sum)%10 ==0:
        return True
    else:
        return False
    
code_num_table = {'0001101':0, '0011001':1, '0010011':2, '0111101':3, '0100011':4,
                  '0110001':5, '0101111':6, '0111011':7, '0110111':8, '0001011':9}
T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    screen = []
    for _ in range(N):
        screen += [input()]

    code_i, code_start_j = find_start(screen)
    code_end_j = find_end(screen)
    find_code_len = len(screen[code_i][code_start_j:code_end_j+1])
    secret_code = ''
    if find_code_len < 56:
        secret_code += '0'*(56-find_code_len) + screen[code_i][code_start_j:code_end_j+1]

    need_to_solve = div_secret_code(secret_code)
    result = []
    for k in range(8):
        result += [code_num_table[need_to_solve[k]]]
    if check_code(result) == True:
        print(f"#{tc} {sum(result)}")
    else:
        print(f"#{tc} 0")