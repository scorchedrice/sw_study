def order(T):
    if T <= 6:
        order(2*T)
        print(node[T])
        order(2*T + 1)
        

node = [0, 'A', 'B', 'C', 'D','E','G']
order(1)