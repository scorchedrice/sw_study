# N이 주어지면 X**3으로 표현할 수 있는 양의 정수 X를 구해라.
def find_prime(n):
    result = []
    for num in range(2,n+1):
        for i in range(2,num):
            if num % i == 0:
                break
        else:
            result += [num]
    
    result = list(set(result))
    result.sort()
    return result

def factorization(n):
    start_num = n
    prime_list = find_prime(n)
    result = []
    while start_num != 1:
        for prime_num in prime_list:
            if start_num%prime_num == 0:
                result += [prime_num]
                start_num = start_num//prime_num
                break
    return result

def check_triple(n):
    factorization_list = factorization(n)
    num_list = list(set(factorization_list))
    check_list = [0]*(len(num_list))
    for i in range(len(num_list)):
        my_num = factorization_list.count(num_list[i])
        if my_num%3 == 0:
            check_list[i] += my_num
        else:
            return -1
    result = 0
    for j in range(len(num_list)):
        result = num_list[j]**(check_list[j]//3)
    return result

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    print(f"#{tc} {check_triple(n)}")