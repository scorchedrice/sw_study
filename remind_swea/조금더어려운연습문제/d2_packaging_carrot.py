'''
1. 같은 크기의 당근은 같은 상자
2. 한 상자에 N/2개를 초과하는 당근이 있어선 안된다.
앞의 조건을 만족하면서 각 상자에 든 당근의 개수 차가 최소가 되도록 포장해야한다.
'''

def carrot_packaging(carrot_list):
    total = []
    num_list = []
    for i in range(0,N-2):
        small = []
        if carrot_list[i] == carrot_list[i+1]:
            continue
        else:
            if len(carrot_list[0:i+1]) > N//2:
                continue
            else:
                small += carrot_list[0:i+1]
        
        for j in range(i+1,N-1):
            mid = []
            big = []
            if carrot_list[j] == carrot_list[j+1]:
                continue
            else:
                if len(carrot_list[i+1:j+1]) > N//2:
                    continue
                else:
                    mid += carrot_list[i+1:j+1]
                if len(carrot_list[j+1:]) > N//2:
                    continue
                else:
                    big += carrot_list[j+1:]
            total += [(small,mid,big)]
            cal_max_min = [len(small), len(mid), len(big)]
            num_list += [(max(cal_max_min)-min(cal_max_min))]
    if total == []:
        return -1
    else:
        return min(num_list)
        
T=int(input())
for tc in range(1,T+1):
    N = int(input())
    carrot_list = list(map(int,input().split()))
    carrot_list.sort()
    print(f"#{tc} {carrot_packaging(carrot_list)}")