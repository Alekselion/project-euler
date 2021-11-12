def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b


task = "What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"
result = 1
for i in range(11, 21):
    result *= i // gcd(i, result)

print(f"Task: {task}\nAnswer: {result}")