def reverse_and_double(n: int) -> int:
    c=0
    p=1
    if n<0:
        p=-1
        n=abs(n)
    while(n):
        c=c*10+n%10
        n=int(n/10)
    return 2*c*p
n=int(input())
print(reverse_and_double(n))