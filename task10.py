def primes(num):
    sieve = [1] * num
    for i in range(3, int(num ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [0] * ((num - i * i - 1) // (2 * i) + 1)
    return [1, 2] + [i for i in range(3, num, 2) if sieve[i]]


task = "Find the sum of all the primes below 2 000 000."
result = (sum(primes(2000000)))
print(f"Task: {task}\nAnswer: {result}")