import math

task = "What is the value of the first triangle number to have over five hundred divisors?"
x, n = 3, 2
while n <= 500:
    n = 2
    result = sum([c for c in range(1, x+1)])
    for i in range(2, math.ceil(result**0.5)):
        if result % i == 0:
            n += 2
        elif (math.ceil(result**0.5))**2 == result:
            n -= 1
        x += 1

print(f"Task: {task}\nAnswer: {result}")