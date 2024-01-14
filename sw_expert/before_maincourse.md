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
#### `input().split()`
- `input()` : 뭘 입력할래
- `.split()` : 입력한 것을 쪼개 무엇을 기준으로

