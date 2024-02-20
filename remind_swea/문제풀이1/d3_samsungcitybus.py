'''
버스정류장 1번부터 5000번까지
버스노선 N개, Ai이상 Bi이하인 모든 정류장만을 다니는 버스노선
P개의 버스 정류장에 대해 각 정류장에 몇개의 버스노선이 다니는지 구하는 프로그램 작성
'''

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    all_station_info = [0] * (5001)
    line_info = []
    for _ in range(N):
        Ai, Bi = map(int,input().split())
        line_info += [[Ai, Bi]]
    # 버스 노선의 정보 입력
    for m in range(N):
        start = line_info[m][0]
        end = line_info[m][1]
        for n in range(start,end+1):
            all_station_info[n] += 1

    P = int(input())
    C_list = []
    for _ in range(P):
        C_list += [int(input())]    
    # 확인해야 할 정류장 정보 입력

    print(f"#{tc}", end = ' ')
    for l in range(P):
        print(all_station_info[C_list[l]], end = ' ')
    print()