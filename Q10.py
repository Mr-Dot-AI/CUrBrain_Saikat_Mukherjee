def countPrimes(n):
    if n <= 2:
        return 0

    # Initially, assume every number is prime
    prime = [True] * n
    prime[0] = prime[1] = False

    # Eliminate multiples of each prime
    for i in range(2, int(n**0.5) + 1):
        if prime[i]:
            for j in range(i * i, n, i):
                prime[j] = False

    # Count the remaining prime numbers
    return sum(prime)


n = int(input())
print(countPrimes(n))