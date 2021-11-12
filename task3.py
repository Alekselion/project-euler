task = "What is the largest prime factor of the number 600 851 475 143?"
num = 600851475143
d = 2
while d * d <= num:
    if num % d == 0:
        num //= d
    else:
        d += 1

print(f"Task: {task}\nAnswer: {num}")

# #############
# FIRST VERSION
# #############

# def check_prime(n):
#     d = 2
#     while d * d <= n and n % d != 0:
#         d += 1
#     return d * d > n


# num = 600851475143
# col = []
# for d1 in range(1, num // 2 + 1):
#     if num % d1 == 0:
#         if d1 in col:
#             break
#         d2 = int(num / d1)
#         col.append(d1)
#         col.append(d2)

# for i in col:
#     if not check_prime(i):
#         col.remove(i)
# res = max(col)
