task = "What is the sum of the digits of the number 2 to power of 1000?"
result = sum([int(x) for x in str(2 ** 1000)])
print(f"Task: {task}\nAnswer: {result}")
