n=int(input("Enter a number:"))
m=n
while(True):
    m=m+1
    for i in range(2,int(m**0.5)):
        if m%i==0: break
    else:
        print(f"The smallest prime number after {n} is {m}.")
        break