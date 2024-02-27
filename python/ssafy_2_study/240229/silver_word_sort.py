word_list = []
word_list_detail = []
N = int(input()) # 단어의 수
for _ in range(N):
    word_list += [input()]
word_list = set(word_list) # 중복 단어 제거

for k in word_list: # 단어 수 별로 정렬하기 위해 (단어길이, 단어)로 구성된 리스트 형성 후 sort
    len_k = len(k)
    word_list_detail += [(len_k, k)]
word_list_detail.sort()

for l in range(len(word_list)):
    print(word_list_detail[l][1])
    