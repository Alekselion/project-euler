task = "There exists exactly one Pythagorean triplet for which a + b + c = 1 000. Find the product abc."
# (a < b < c) AND (a^2 + b^2 = c^2) AND (a + b + c = 1000)
for a in range(1, 501):
    for b in range(2, 501):
        c = (a ** 2 + b ** 2) ** 0.5
        if a + b + c == 1000 and a < b:
            result = a * b * int(c)
            break

print(f"Task: {task}\nAnswer: {result}")