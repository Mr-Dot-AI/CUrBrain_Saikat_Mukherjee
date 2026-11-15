def reverse(l):
    for i in range(len(l)//2):
        l[i],l[len(l)-1-i]=l[len(l)-1-i],l[i]
    return l

l=list(map(int,input("Enter the elements: ").split()))
k=int(input("Enter the value of k: "))
if k<0:
    print("K can not be less than 0.")
k=k%len(l)
l=reverse(l)
l1=reverse(l[:k])
l1.extend(reverse(l[k:]))
print(l1)