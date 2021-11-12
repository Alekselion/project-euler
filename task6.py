task = "Find the difference between the sum of the squares of the 1-st 100 natural numbers and the square of the sum."
one_hundred_num = [i for i in range(1, 101)]
pow_num = [j ** 2 for j in range(1, 101)]
result = (sum(one_hundred_num) ** 2) - sum(pow_num)
print(f"Task: {task}\nAnswer: {result}")