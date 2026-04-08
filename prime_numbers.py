def primes(n):
    for num in range(2, n+1):
        for i in range(2, num):
            if num % i == 0:
               break
        else:
            yield num
limit = int(input("generate prime numbers upto:" ))
print(f"prime numbers upto", (limit))
for prime in primes(limit):
    print(prime, end=" ")
