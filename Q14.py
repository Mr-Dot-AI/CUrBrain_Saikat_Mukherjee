l=list(map(int,input("Enter the array of numbers: ").split())) 
k=int(input("Enter the thresshold: "))
if k<0:
    print("Thresshold can not be negative.")
for i in l[:]:
    if i<0:
        print("You entered a negative value in the list.")
    if i<k:
        l.remove(i)
print(l)