def fibonacci(num):
    fib = [1, 1]
    for i in range(2, num):
        fib.append(fib[i - 1] + fib[i - 2])
        if fib[-1] >= 4000000:
            fib.remove(fib[-1])
            return fib


task = "By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms."
series = fibonacci(1000)
result = sum([num for num in series if num % 2 == 0])
print(f"Task: {task}\nAnswer: {result}")

