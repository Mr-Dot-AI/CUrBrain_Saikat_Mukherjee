def func(n: int)-> int:
    d=0
    p,s=1,0
    if n<0:
        p=-1
        n=abs(n)
    
    while(n):
        d=n%10
        p*=d
        s+=d
        n=int(n/10)
    return p-s
n=int(input())
print(func(n))