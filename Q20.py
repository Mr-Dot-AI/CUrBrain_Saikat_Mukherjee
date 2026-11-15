l=list(map(int,input("Enter the elements: ").split()))
s=0
if not l:
    print("The array is empty.")
    exit(1)
for i in range(len(l)-1,-1,-1):
    prev=l[i]
    l[i]=s
    s+=prev

print(l)