import math

def my_result(input_num):
    a = input_num+1
    b = -1
    result = 0
    if input_num % 2 == 0:
        for i in range(30):
                a -= 1
                b += 1
                result += (2**b)*math.comb(a,b)
             
                if a == b:
                    break
    else:
        for j in range(30):
            a -= 1
            b += 1
            result += (2**b)*math.comb(a,b)
            
            if a-b == 1:
                break
    return result

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    input_num = N//10
    print(f"#{tc} {my_result(input_num)}")