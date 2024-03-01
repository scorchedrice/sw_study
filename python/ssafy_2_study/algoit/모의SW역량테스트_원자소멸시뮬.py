# 못..해!

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
'''
시간은 중요하지 않으니, 충돌 가능성을 조사하고, 이 에너지들의 총합을 구하자.
한 원자를 기준으로 하나씩 가면서, 상하좌우에 있는 것을 확인한다. (x좌표절대값 혹은 y좌표절대값 차 0인경우)
더불어 그것들의 이동 방향을 확인한다.
그곳까지 갔을 때 시간과, 그 때 해당 원자의 위치를 계산하고
과연 충돌이 가능한지 판별한 후 에너지를 추가한다.
'''
# 이차원 좌표 경계를 -2000, 2000으로 두고 한칸씩 보는 것이 편리
# 2000을 더해 양수로 보정해도 편리
N = int(input())
atoms = []
atom_position = [[0 for _ in range(4001)] for _ in range(4001)]
for _ in range(N):
    # x,y,dir,E
    x,y,dir,E = map(int,input().split())
    x = 2*(x+1000)
    y = 2*(y+1000)
    atoms.append([x,y,dir,E])
    atom_position[x][y] += 1
# dir 0(y +), 1(y -), 2(x +), 3(x -)
change = [(0,1),(0,-1),(1,0),(-1,0)]
finished_atoms = []
crash_atoms = set()
total_E = 0
while atoms:
    for i in range(len(atoms)):
        x,y,dir,E = atoms[i]
        move_x = x + change[dir][0]
        move_y = y + change[dir][1]
        if move_x < 0 or move_x > 4000 or move_y < 0 or move_y > 4000:
            finished_atoms.append(i)
            continue
        atom_position[x][y] -= 1
        atom_position[move_x][move_y] += 1
        atoms[i][0] = move_x
        atoms[i][1] = move_y
    if finished_atoms != []:
        for i in range(len(finished_atoms)):
            del_atom_num = finished_atoms.pop()
            del_x, del_y = atoms[del_atom_num][0], atoms[del_atom_num][1]
            atom_position[del_x][del_y] -= 1
            atoms.pop(del_atom_num)
    for i in atoms:
        x,y = i[0], i[1]
        if atom_position[x][y] > 1:
            crash_atoms.add((x,y))
    if crash_atoms:
        for x,y in crash_atoms:
            for i in range(len(atoms)-1,-1,-1):
                x_p, y_p, e = atoms[i][0], atoms[i][1], atoms[i][3]
                if x_p == x and y_p == y:
                    atom_position[x_p][y_p] -= 1
                    total_E += e
                    atoms.pop(i)
        crash_atoms.clear()
print(total_E)


