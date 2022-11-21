str1 = input()
str2 = input()

last_char = str2[-1]
cnt = 0

for i in str1:
    if i== last_char:
        cnt += 1

print(cnt)


