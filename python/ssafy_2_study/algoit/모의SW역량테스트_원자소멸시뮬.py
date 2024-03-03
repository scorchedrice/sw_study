'''
원자들은 2차원 평면에서 이동하며, 두 원자가 충돌하는 경우 에너지를 방출하고 소멸된다.
2차원 평면 (x,y)를 활용한다.
원자가 이동하는 방향은 상, 하, 좌, 우 중 하나
모든 원자들의 이동 속도는 동일하다 (1초에 한칸 이동)
    - 이동속도가 동일하므로 0.5로 쪼개는 경우 고려해야 할 수 있음
모든 원자들은 최초위치에서 동시에 이동을 시작한다
두 개 이상의 원자가 동시에 충돌한 경우 (여러개가 동시 충돌할 수 있네) 에너지 방출 후 소멸
'''
'''
원자들의 개수는 1개이상 1000개이하
에너지는 1이상 100이하의 값
x와 y좌표는 -1000이상 1000이하이다.
상(0) 하(1) 좌(2) 우(3)
'''
# 이차원 좌표 경계를 -2000, 2000으로 두고 한칸씩 보는 것이 편리
# 문제에서 주어지는 평면은 x,y평면으로 혼동 주의
# 상하좌우[(0,1),(0,-1),(-1,0),(1,0)]

dir = [(0,1),(0,-1),(-1,0),(1,0)]
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    atom_list = []
    for _ in range(N):
        atom_info = list(map(int,input().split()))
        atom_info[0] *= 2
        atom_info[1] *= 2
        # 좌표를 두배로 본 것 적용
        atom_list.append(atom_info)
        # x좌표, y좌표, 방향, 가지고 있는 에너지


    total_E = 0
    while True:
        if atom_list == []: # 모든 원자들이 제거되는 경우 반복 중단
            break

        for i in range(len(atom_list)):
            dir_info = atom_list[i][2]
            atom_list[i][0] = atom_list[i][0] + dir[dir_info][0]
            atom_list[i][1] = atom_list[i][1] + dir[dir_info][1]
        # 원자 이동시키는 과정 진행 후, 좌표가 겹치는 것이 있는 것을 확인한다.
        visited = set()
        del_atom = set()
        for j in range(len(atom_list)):
            cx = atom_list[j][0]
            cy = atom_list[j][1]
            if (cx, cy) in visited:
                del_atom.add((cx,cy))
            else:
                visited.add((cx,cy))

        for k in range(len(atom_list)-1, -1, -1):
            # 거꾸로 이를 확인하면 에러를 방지할 수 있다.
            cx = atom_list[k][0]
            cy = atom_list[k][1]
            if (cx, cy) in del_atom:
                total_E += atom_list[k][3]
                del atom_list[k]
            elif cx > 2000 or cx < -2000 or cy > 2000 or cy < -2000:
                del atom_list[k]
        
    print(f"#{tc} {total_E}")