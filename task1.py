task = "Find the sum of all the multiples of 3 or 5 below 1 000."
result = sum([num for num in range(3, 1000) if num % 3 == 0 or num % 5 == 0])
print(f"Task: {task}\nAnswer: {result}")