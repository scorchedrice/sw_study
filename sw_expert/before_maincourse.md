## 1. 가위바위보
```
a, b = map(int, input().split())
def game():
    if (a == 1 and b == 3) or (a == 2 and b ==1) or (a == 3 and b == 2):
        print('A')
    else:
        print('B')
game()
```