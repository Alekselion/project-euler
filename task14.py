from functools import lru_cache


@lru_cache(5000000)
def calc(number):
    if number == 1:
        return 0
    elif number % 2 == 0:
        iterations = calc(number//2)+1
    else:
        iterations = calc(3*number+1)+1
    return iterations


task = "Which starting number, under one million, produces the longest chain?"
max_num, num = 0, 0
for i in range(1, 1000001):
    if (cur_num := calc(i)) > max_num:
        max_num, num = cur_num, i
result = num
print(f"Task: {task}\nAnswer: {result}")