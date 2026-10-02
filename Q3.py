def reversen(n: int) -> int:
    c=0
    p=1
    if n<0:
        p=-1
        n=abs(n)
    while(n):
        c=c*10+n%10
        n=int(n/10)
    return c*p
n=int(input())
if n==reversen(n):
    print(n)
else:
    print(n+reversen(n))