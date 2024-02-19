T = int(input())
for tc in range(1,T+1):
    matrix_size, hit_size = map(int,input().split())
    matrix = []
    for k in range(matrix_size):
        matrix += [list(map(int,input().split()))]

    result = []
    catch = 0
    def catch_fly(i,j):
        catch = 0
        for i in range(i,i+hit_size):
            catch += sum(matrix[i][j:j+hit_size])
        return catch

    for i in range(matrix_size-hit_size+1):
        for j in range(matrix_size-hit_size+1):
            result += [catch_fly(i,j)]

    print(f"#{tc} {max(result)}")