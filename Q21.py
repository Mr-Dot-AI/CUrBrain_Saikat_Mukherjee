l=list(map(int,input("Enter the elements: ").split()))
deleted=False
k=int(input("Enter the value to be deleted: "))

if not l:
    print("Enter the inputs properly.")
    exit(1)
for i in range(len(l)):
    if l[i]==k and not deleted:
        deleted = True
        
    if deleted and i < len(l)-1:
        l[i]=l[i+1]
if deleted:
    l.pop()
print(l)