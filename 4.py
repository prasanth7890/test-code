r=int(input())
c=int(input())

matrix  = []
for i in range(r):
    temp = list(map(int, input().split()))
    matrix.append(temp)


l1=[]
l2=[]
for i in range(r):
    for j in range(c):
        if matrix[i][j]==0:
            l1.append(i)
            l2.append(j)
l2.sort()
t=[(l1[0],l2[0]),(l1[0],l2[-1]),(l1[-1],l2[0]),(l1[-1],l2[-1])]
print(t)
