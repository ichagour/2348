words = input().split()

for word in words:
    cnt = 0
    for w in words:
        if w == word:
            cnt += 1
    print(word, cnt)