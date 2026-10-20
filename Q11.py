def sum_modulo(arr):
    MOD = 1_000_000_007
    result = 0

    for value in arr:
        if value<0:
            print("You have entered a non-negative integer in the array.")
            exit(1)
        result = (result + value % MOD) % MOD

    return result

print(sum_modulo(list(map(int,input().split()))))