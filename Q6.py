n,a,b=map(int, input().split())
if (a>9 or b>9) or n<0:
    print("Invalid Input.")
    exit(1)
if a==b:
    print(0)
else:
    ca,cb=0,0
    if n==0:
        ca= a==0
        cb= b==0
    while(n):
        if n%10==a:
            ca+=1
        if n%10==b:
            cb+=1
        n=int(n/10)
    print(abs(ca-cb))