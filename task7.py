def primes(num):
    sieve = [1] * num
    for i in range(3, int(num ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [0] * ((num - i * i - 1) // (2 * i) + 1)
    return [1, 2] + [i for i in range(3, num, 2) if sieve[i]]


task = "What is the 10 001-st prime number?"
result = primes(1000000)[10001]
print(f"Task: {task}\nAnswer: {result}")
