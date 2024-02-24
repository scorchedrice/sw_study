'''
1부터 연속적으로(index주의) 번호가 붙어있는 스위치
켜져있거나(1) 꺼져있거나(0)
학생들이 할 내용
- 남 : 스위치 번호가 자기가 받은 수 배수라면 그 스위치의 상태를 바꿈
- 여 : 받은 수의 스위치를 중심으로 좌우가 대칭이면서 그 구간에 속한 스위치의 상태를 바꾼다.
   (0 1 1 1 0)이고 3을 받았다면 (3), (2와 4), (1과  5)를 바꾼다.
   만약 (1 1 1 0 1) 이라면 좌우대칭이 깨지므로 (3)만 바꿈
'''
'''
주어지는 input
N (스위치 개수)
스위치 정보
학생 수
성별(남1여2) 숫자
.
.

'''
'''
출력 조건
한 줄에 스위치 정보 20개를 최대로 출력한다.
21개라면 20개를 다 채운 한줄과 하나의 스위치를 다음줄에 표시
'''
'''
여학생인 경우 판별함수 정의
남학생인 경우 판별함수 정의
'''
def boy(num):
    for k in range(1,N+1):
        if k%num == 0:
            if switch[k] == 1:
                switch[k] = 0
            elif switch[k] == 0:
                switch[k] = 1
    return

def girl(num):
    if switch[num] == 1:
        switch[num] = 0
    elif switch[num] == 0:
        switch[num] = 1
    
    cnt = 1
    while True:
        if 1<=num+cnt<=N and 1<=num-cnt<=N:
            if switch[num+cnt] == 1 and switch[num-cnt] == 1:
                switch[num+cnt] = 0
                switch[num-cnt] = 0
            elif switch[num+cnt] == 0 and switch[num-cnt] == 0:
                switch[num+cnt] = 1
                switch[num-cnt] = 1
            else:
                break
            cnt += 1
        else:       
            break

N = int(input()) # 스위치의 개수
switch = [0] + list(map(int,input().split())) # 스위치 정보 입력 (맨 앞 추가해 인덱스 활용)
student = int(input())
for i in range(student):
    sex, num = map(int,input().split()) # 성별과 부여받은 번호 입력
    if sex == 1: # 남학생
        boy(num)
    elif sex == 2:
        girl(num)

if N <= 20:
    print(*switch[1:])
elif N <= 40:
    print(*switch[1:21])
    print(*switch[21:])
elif N <= 60:
    print(*switch[1:21])
    print(*switch[21:41])
    print(*switch[41:])
elif N <= 80:
    print(*switch[1:21])
    print(*switch[21:41])
    print(*switch[41:61])
    print(*switch[61:])
elif N <= 100:
    print(*switch[1:21])
    print(*switch[21:41])
    print(*switch[41:61])
    print(*switch[61:81])
    print(*switch[81:])
