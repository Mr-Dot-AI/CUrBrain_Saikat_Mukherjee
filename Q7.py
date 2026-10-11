l=list(map(int, input().split()))
if len(l)==1:
    print(l[0])
    exit(1)
g=l[0]
for i in l[1:]:
    a,b=g,i

    while b:
        a,b=b,a%b
    g=a
print(g)