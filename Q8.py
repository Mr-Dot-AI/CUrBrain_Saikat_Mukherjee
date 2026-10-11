n=int(input("Enter n: "))
k=int(input("Enter k: "))
f=[]
if n<0 or k<0:
    print("n and k cannot be negative.")
    exit()
for i in range(1,int(n**0.5)):
    if n%i==0:
        f.append(i)
        f.append(n//i)
f.sort()
try:
    if f[k+1]:
        print(f[k+1])
except IndexError:
    print(-1)