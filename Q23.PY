l = list(map(int, input().split()))

if not l:
    print("Array cannot have 0 elements.")
    exit(1)

sum = l[0]
presum = l[0]

for e in l[1:]:
    sum = e if e < (sum + e) else sum + e
    presum = min(presum, sum)

print(presum)