n  = int(input())
f = False

if n < 0:
    f = True
n = abs(n)
res = ""
while n>=3:
    res+=str(n%3)
    n = n//3
res = res[::-1]
res =  str(n) +res

if f:
    print('-' + res)
else:
    print(res)



