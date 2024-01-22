t = int(input())
for i in range(1, t+1):
    a = list(map(str, input()))
    for j in range(1,10):
        if a[0:j] == a[j:2*j] and len(a[0:j]):
            if len(a[0:j]) == 2:
            	print(f"#{i} {2}")
            
            elif len(a[0:j]) == 3:
                print(f"#{i} {3}")

            elif len(a[0:j]) == 4:
                print(f"#{i} {4}")
            print(f"#{i} {len(a[0:j])}")
            continue
        elif a[0:j] == a[j:2*j] and len(a[0:j]) >= 5:
            print(f"#{i} {len(a[0:j])}")