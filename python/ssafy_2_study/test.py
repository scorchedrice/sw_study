T = int(input())
name_score = []
count_list = [0] * 101 #0을 포함

for tc in range(1,T+1):
    name_score += [list(map(str, input().split()))] # 입력 값 받기
    
score_list = []
for i in range(0, T):
    score_list = score_list + [int(name_score[i][1])] # 성적을 받고 이를 리스트화 (str으로 받았으니 int로 다시 전환하는 과정 필)

for j in range(0,100): # 해당 점수가 몇번 나왔는지 표시하는 과정
    for num in score_list:
        if num == j:
            count_list[j] += 1

for index in range(0,len(count_list)): # count_list를 탐색하는 과정
    if count_list[index] != 0: 
        count_list[index] -= 1 
        for k in range(0, len(name_score)): # 0이 아닌경우(언급이 하나라도 된 경우), 1 빼고 돌리는 for 문
            if name_score[k][1] == str(index): # 위에서 입력받은 이름과 성적 리스트의 성적이 index와 같다면 (str으로 받음)
                print(name_score[k][0], end = ' ') # 그 값과 일치하는 이름을 출력한다.