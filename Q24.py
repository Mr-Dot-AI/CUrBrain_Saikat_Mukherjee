l = list(map(int, input().split()))
target=int(input())
if not l:
    print(0)
    exit(1)
if len(l)==1:
    print(l[0])
    exit(1)
im=len(l)
flag=0
for i in range(len(l)):
    sum=0
    for j in range(i,len(l)):
        sum+= l[j]
        if sum>=target:
            im=min(im,j-i+1)
            flag=1
            break
print(im if flag else 0)
        