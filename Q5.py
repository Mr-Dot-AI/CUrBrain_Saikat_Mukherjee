n=int(input())
l=[]
if n==0:
    print([0])
    exit(1)
elif n<0:
    print("Invalid Input: Negative Numbers.")
    exit(1)
while(n):
    if n%2:
        l.append(n%10)
    else:
        l.append(0)

    n=int(n/10)

print(list(reversed(l)))