T = int(input())
for tc in range(1,T+1):
    word, macro = input().split()
    word = list(word)
    macro = list(macro)
    macro_len = len(macro)
 
    use_macro = 0
    while True:
        word_len = len(word)
        recent_use_macro = use_macro
        for k in range(word_len - macro_len + 1):
            if word[k:k+macro_len] == macro:
                use_macro += 1
                del word[k:k+macro_len]
                break
        if recent_use_macro == use_macro:
            break
        elif len(word) < macro_len:
            break
    print(f"#{tc} {use_macro + len(word)}")