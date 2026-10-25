l=list(map(int,input("Enter the array of numbers: ").split())) 
if not l:
    print("The list is empty.")
else:
    low=l[0]
for i in l[1:]:
    if abs(i)<abs(low):
        low=i
print(low)