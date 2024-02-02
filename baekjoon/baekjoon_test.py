def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]
    right = [num for num in tail if num > pivot]
    left = [num for num in tail if num <= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

def sort_codenum(word_list):
    result = []
    for i in range(len(word_list)):
        word_length = len(word_list[i])   
        code_list = ''
        for j in range(word_length): 
            my_str = str(ord(word_list[i][j]))
            if ord(word_list[i][j]) < 100:
                my_str = '0' + str(ord(word_list[i][j]))
            code_list = code_list + my_str
        result += [int(code_list)]
    result = quick_sort(result)
    for i in range(len(result)):
        result[i] = str(result[i])
    
    for k in range(len(result)):
        if result[k][0:2] == '97' or result[k][0:2] == '98' or result[k][0:2] == '99':
            result[k] = '0' + result[k]
    return result

T = int(input())
word_list = []
for tc in range(1, T+1):
    word_list += list(map(str, input().split()))

word_list = sort_codenum(list(set(word_list)))

for i in range(len(word_list)):
    result_1 = ''
    for j in range(int(len(word_list[i])/3)):
        result_1 += chr(int(word_list[i][3*j] + word_list[i][j*3+1] + word_list[i][j*3+2]))
    print(result_1)
