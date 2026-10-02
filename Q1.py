n=int(input())
c=0
while(n):
    c+=1
    n=int(n/10)
if c%2:
    print(False)
else:
    print(True)