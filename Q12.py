base=int(input('Enter the base:'))
power=int(input('Enter the power:'))
mod=int(input('Enter the mod:'))
if base<0 or power<0 or mod<=0:
    print("Invalid Input.")
    exit(1)
result=1
for i in range(power):
    result*=base
print(result%mod)
