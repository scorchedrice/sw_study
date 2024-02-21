T = int(input())
for tc in range(1,T+1):
    word, macro = input().split()
    word_len = len(word)
    macro_len = len(macro)
    # 고려할 인덱스는 0부터 word_len - macro_len
    now = 0
    use_macro = 0
    just_type = 0
    while True:
        if now >= word_len:
            break
        if word[now:now+macro_len] == macro:
            use_macro += 1
            now += macro_len
        else:
            just_type += 1
            now += 1
    print(use_macro)
    print(just_type)