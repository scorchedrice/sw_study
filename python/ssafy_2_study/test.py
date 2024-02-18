# 커리큘럼
'''
N개의 강의 (1번부터 N번까지)
동시에 여러 강의를 들을 수 있다고 가정한다.
'''
from collections import deque

N = int(input())
class_list = [[] for _ in range(N+1)]
time_list = [0] * (N+1)
indegree = [0] * (N+1)

for k in range(1,N+1):
    data = list(map(int,input().split()))
    time_list[k] += data[0]
    for x in data[1:-1]:
        indegree[x] += 1
        class_list[x] += [k]
# class_list에 들어야하는 수업의 번호, 그 수업이 어떤 과목의 선수과목인지 입력
print(class_list)
print(indegree)
print(time_list)
def topo_sort():
    result = [0] * (N+1)
    Q = deque()

    for i in range(1,N+1):
        if indegree[i] == 0:
            # 진입 차수가 0인경우
            Q.append(i)
            result[i] += time_list[i]
        
    while Q:
        current = Q.popleft()
        for j in class_list[current]:
            result[j] += time_list[j] + result[current]
            indegree[j] -= 1
            if indegree[j] == 0:
                Q.append(j)
        
    for i in range(1,N+1):
        print(result[i])

topo_sort()




