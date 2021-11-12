task = "Find the largest palindrome made from the product of two 3-digit numbers."
result = []
for a in range(1000, 100, -1):
    for b in range(1000, 100, -1):
        number = str(a * b)
        rev_number = str(number[::-1])
        if number == rev_number:
            result.append(int(number))
result = max(result)
print(f"Task: {task}\nAnswer: {result}")