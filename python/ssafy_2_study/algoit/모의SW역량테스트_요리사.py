'''
N(식재료)은 항상 짝수로 주어지므로 2로 나눌 때 문제 없음
식재료를 반으로 나눠 두개의 음식을 만들 예정
이 때, 두 음식의 맛 점수가 동일하도록 재료를 분배해야한다.
맛 점수는 주어진 테이블을 활용한다. (i,j를 활용하는 경우 table[i][j] + table[j][i])
'''
'''
주어진 식재료를 반 나누는 함수 정의 (부분집합, 크기는 n//2로 구하면 나머지는 정해짐
해당 식재료를 2개씩 부분집합 구하기, 이 때 점수를 구한다.
'''
def div_material(arr):
    global A_material
    global B_material
    for i in range(1<<N):
        memory = []
        for j in range(N):
            if i & (1<<j):
               memory += [arr[j]]
        if len(memory) == N//2:
            A_material.append(memory)
            B_material.append(list(set(arr) - set(memory)))

def food_score(arr):
    len_arr = len(arr)
    result = []
    for i in range(1<<len_arr):
        memory = []
        for j in range(len_arr):
            if i & (1<<j):
               memory += [arr[j]]
        if len(memory) == 2:
            a = memory[0]
            b = memory[1]
            result.append(table[a][b] + table[b][a])
    return sum(result)

# T = int(input())
# for tc in range(1,T+1):
N = int(input()) # 식재료 개수
table = []
for _ in range(N):
    table.append(list(map(int,input().split())))
material = list(range(0,N))
A_material = []
B_material = []
div_material(material)
print(A_material)
print(B_material)

diff_score = []

for k in range(len(A_material)):
    score_A = food_score(A_material[k])
    score_B = food_score(B_material[k])
    diff_score.append(abs(score_A - score_B))
print(diff_score)
