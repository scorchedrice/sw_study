# 커리큘럼
'''
N개의 강의 (1번부터 N번까지)
동시에 여러 강의를 들을 수 있다고 가정한다.
'''
'''
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
'''
N = int(input())

time_list = [0] * (N+1)
# index에 해당하는 수업을 듣는데 소요되는 시간리스트
result = [0] * (N+1)
# 결과에 사용할 시간리스트
class_list = [[] for _ in range(N+1)]
# index에 해당하는 수업이 어떤 수업의 선수수업인지 기록하기 위한 리스트
indegree = [0] * (N+1)
# 해당 수업이 몇개의 수업을 들어야 들을 수 있는 수업인지 기록하기 위한 리스트

for _ in range(1,N+1):
    info = list(map(int,input().split()))
    time_list[_] += info[0]
    result[_] += info[0] # copy.deepcopy(time) 대체
    for x in info[1:-1]:
        class_list[x] += [_]
        indegree[_] += 1

Q = []
for k in range(1,len(indegree)):
    if indegree[k] == 0:
        Q.append(k)
        # indegree : [0, 0, 1, 1, 2, 1]

while Q:
    current = Q.pop(0)
    for i in class_list[current]:
        '''
        class_list : [[], [2, 3, 4], [], [4, 5], [], []]
        time_list : [0, 10, 10, 4, 4, 3]
        '''
        result[i] = result[current] + time_list[i]
        # 문제 예시처럼 max를 써야하는 이유가 무엇? 스터디에서 물어보기
        '''
        현 위치의 class_list를 확인했을 때, 
        해당 과목을 필요로 하는 과목의 번호 result를 수정한다.
        그 값은 current과목 시간 + 해당 과목의 시간으로 정의할 수 있다.
        '''
        '''
        순서
        CURRENT = 1
        - 2를 i로 가져온 경우
        result[2] = result[1] + time_list[2]
        result = [0,10,20,4,4,3]
        indegree = [0,0,1,1,2,1] -> [0,0,0,1,2,1]
        Q = [2]
        - 3을 i로 가져온 경우
        result[3] = result[1] + time_list[3]
        result = [0,10,20,14,4,3]
        indegree = [0,0,0,1,2,1] -> [0,0,0,0,2,1]
        Q = [2,3]
        - 4를 i로 가져온 경우
        result[4] = result[1] + time_list[4]
        result = [0,10,20,14,14,3]
        indegree = [0,0,0,0,2,1] -> [0,0,0,0,1,1]
        Q = [2,3]

        CURRENT = 2
        pass
        Q = [3]

        CURRENT = 3
        Q = []
        - 4를 i로 가져온 경우
        result[4] = result[3] + time_list[4]
        result = [0,10,20,14,18,3]
        indegree = [0,0,0,0,2,1] -> [0,0,0,0,0,1]
        Q = [4]
        - 5를 i로 가져온 경우
        result[5] = result[3] + time_list[5]
        result = [0,10,20,14,18,17]
        indegree = [0,0,0,0,2,1] -> [0,0,0,0,0,0]

        CURRENT = 4
        Q = []
        '''
        indegree[i] -= 1
        if indegree[i] ==0:
            Q.append(i)

for k in range(1,N+1):
    print(result[k])