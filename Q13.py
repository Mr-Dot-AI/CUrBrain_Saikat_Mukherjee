l=list(map(int,input("Enter the numbers: ").split()))
k=int(input("Enter the value of modulo: "))
if k==0:
    print("Invalid Input")
k=abs(k)
n=[l[0]]
if len(l)!=1:
    for i in range(1,len(l)):
        n.append(l[i]+n[i-1])
        if n[i-1]%k==0:
            print(True)
            break
    else:
        if n[-1]%k==0:
            print(True)
        else:
            print(False)
else: print(not(bool(n[0]%k)))