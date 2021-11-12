task = "Find the sum of the digits in the number 100!"
factorial = 1
for res in range(100, 0, -1):
    factorial *= res
result = sum([int(x) for x in str(factorial)])
print(f"Task: {task}\nAnswer: {result}")
